# -*- coding: UTF-8 -*-
'''
Created on 2015-1-27

@author: L
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from urllib2 import URLError,HTTPError,urlopen
import time
import tempfile
import BeautifulSoup
import mechanize
from socket import error
import traceback
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

errors = {10054:u'链接被重置',
          10060:u'链接超时',
          10061:u'链接被拒绝',
          0:u'发送有误',
          400:u'请求无效',
          403:u'禁止访问',
          404:u'无法找到文件',
          405:u'资源被禁止',
          406:u'无法接受',
          407:u'要求身份验证',
          500:u'服务器有误',
          502:u'网关错误',
          503:u'服务不存在',
          504:u'网关超时',
          10000:u'socket错误',
          10001:u'其他错误，无法访问',
          10053:u'服务器主动断开'}

class Link(object):
    def __init__(self,url,channel,text='',code=200):
        self.url = url
        self.channel = channel
        self.text = text
        self.code = code
    
    def set_code(self,code):
        self.code = code
    
    def set_text(self,text):
        self.text = text
    
    def set_channel(self,channel):
        self.channel = channel


def get_response(url,times=1,wait=1):
    assert isinstance(url,(str,unicode)),'[get_response] Param url must be a string'
    
    num = times
    response = None
    
    while num:
        try:
            response = urlopen(url,timeout=30)
            if response:
                num = 0
        except Exception,e:
            time.sleep(wait)
            num -= 1
            if num == 0:
                raise e
            
    return response

def test_404(url):
    code = None
    try:
        #response = get_response(url,times=1)
        html = requests.get(url, allow_redirects=False, timeout=0.1)
        code =html.status_code
    except HTTPError,e:
        code = e.code
    except (URLError,error),e:
        try:
            code = str(e.args[0].errno)
        except:
            code = 10000 
    except HTTPError,e:
        code = e.code
    except:
        code = 10001 

    return code

def multi_test_404(url,times=2,wait=1):
    for i in xrange(times):
        code = test_404(url)
        if 200 == code:
            break
        time.sleep(wait)

    return (url,code)


def test_location(url):
    location  = None
    try:
        #response = get_response(url,times=1)
        headers = requests.head(url).headers
        if headers['location']:
            location =  headers['location']
    except KeyError:
        pass

    return location
def get_response_page(url,times=3,wait=10):
    assert isinstance(url,(str,unicode)),'[get_response] Param url must be a string'
    
    num = times
    response = None
    page = None
    
    while num:
        try:
            response = urlopen(url,timeout=30)
            if response:
                page = response.read()
                response.close()
                num = 0
        except:
            time.sleep(wait)
            num -= 1
            
    return page


def response_in_tempfile(url,times=3,wait=10):
    page = get_response_page(url,times,wait)
    
    temp = tempfile.TemporaryFile()
    if page:
        temp.write(page)
        temp.seek(0)
            
    return temp


# def getrecommendedurl(chanel_url):
#     page = get_response_page(chanel_url,8)
#     
#     result = []
#     for parser in ('html5lib', 'lxml', 'html.parser'):
#         vhtml = None
#         try:
#             soup = BeautifulSoup.BeautifulSoup(page,parser)
#             vhtml =soup.find("ul",{'class':"letv-tui-ul"})
#         except:
#             continue
#         
#         if not vhtml:
#             return []
#         
#         urls =vhtml.findAll("a")
#         result = result + [i['href'] for i in urls]
#         
#     return list(set(result))

def getrecommendedurl(chanel_url):
    page = get_response_page(chanel_url,8)
    
    result = []
    try:
        soup = BeautifulSoup.BeautifulSoup(page)
        vhtml =soup.find("ul",{'class':"letv-tui-ul"})
        if vhtml:
            urls =vhtml.findAll("a")
            result = result + [i['href'] for i in urls]
    except :
        #
        traceback.print_exc()
        
    return list(set(result))
    
def get_response_urls(url):
    page = get_response_page(url,8)
    if not page:
        raise RuntimeError("Can not get the page [%s] !"%str(url))
    
    print page
    soup = BeautifulSoup.BeautifulSoup(page)
    hrefs = soup.findAll('a', recursive=True)
    
    if not hrefs:
        return []
    
    result = [url['href'] for url in hrefs if url.has_key('href')]
    
    return list(set(result))


def get_response_urls_m(channel_url):
    lf = mechanize.LinksFactory()
    response = response_in_tempfile(channel_url)
    lf.set_response(response,channel_url,'utf-8')
    
    links = []
    [ links.append(Link(link.url,channel_url,link.text)) for link in lf.links() if not links.count(link) and not link.url.startswith('javascript')]
        
    response.close()

    return links


# # 
# if __name__ == "__main__":
#     c = get_response_urls_m('http://fun.le.com/')
#     for  i  in c:
#         print i.url,i.text
#     code = multi_test_404('http://www.letv.com/ptv/vplay/23154311.html')
#     print code
#     get_response('http://www.letv.com/ptv/vplay/23154311.html')
#     print 'end'
    