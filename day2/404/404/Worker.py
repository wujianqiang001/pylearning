# -*- coding: UTF-8 -*-
'''
Created on 2015-7-7


'''

import BeautifulSoup
import Response
from multiprocessing.dummy import Pool as ThreadPool
import mechanize
import MailSender
import sys
import time
import os

# def synchronized(lock):
#     """ Synchronization decorator.
#              同步锁，用来锁住争抢资源
#     """
#     def wrap(f):
#         def newFunction(*args,**kw):
#             lock.acquire()
#             try:
#                 return f(*args,**kw)
#             finally:
#                 lock.release()
#         return newFunction
#     return wrap


class Worker:
    links = []
    errlinks = []
    recommendlinkdict = {}

    @staticmethod
    def clear_result():
        Worker.errlinks = []

    @staticmethod
    def store_channel_links(channels,threadnum=5):
        channel_pool = ThreadPool(threadnum)
        result = channel_pool.map(Response.get_response_urls_m, channels)
        #result = channel_pool.map(Response.get_response_urls, channels)
        channel_pool.terminate()
        channel_pool.close()

        for urls in result:

            Worker.links = Worker.links + urls

        return

    @staticmethod
    def get_urls():
        urls = []
        #[urls.append(link.url) for link in Worker.links if not urls.count(link.url)]
        [urls.append(link.url.replace('//','http://')) if not urls.count(link.url) and link.url.startswith('//')   else urls.append(link.url) for link in Worker.links ]

        return urls

    @staticmethod
    def store_recommended_links(channels):
        for channel in channels:
            print channel
            urls = Response.getrecommendedurl(channel)
            print urls
            if urls:
                Worker.recommendlinkdict[channel] = urls

        return

    @staticmethod
    def start_test(threadnum=8):
        urls = Worker.get_urls()

        pool = ThreadPool(threadnum)
        result = pool.map(Response.multi_test_404, urls)
        pool.terminate()
        pool.close()
        print result

        errsdict = {}
        for t in result:
            if t[1] == 'None':
                break

            if  302 == int(t[1]):
                location = Response.test_location(t[0])
                if location != None and location.find('error/?msg') != -1:
                   print str(t[0]) + '  : ' + str(t[1])
                   errsdict[t[0]] = t[1]

        if not errsdict:
            return

        errs = errsdict.keys()


        for link in Worker.links:
            if errs.count(link.url):
                link.set_code(errsdict[link.url])
                Worker.errlinks.append(link)


            else:
                link.set_code(200)

        return len(urls)

    @staticmethod
    def send_result_mail(start_time,end_time):
        testnum = len(Worker.links)
        errnum  = len(Worker.errlinks)
        testname = u'PC主站 404错误测试'
        content = MailSender.generate_result_content(start_time, end_time, testname, testnum, errnum)
        MailSender.send_mail('songjie@letv.com','songjie@letv.com','Test',content,[])

        return

    @staticmethod
    def test_and_record(start_time,end_time):
        testname = u'PC主站 404错误测试'
        testnum = len(Worker.links)
        errnum = len(Worker.errlinks)
        with open ('result.txt','a') as fh:
            fh.writelines(str(start_time) + ';'+ str(end_time) + ';' + testname + ';' + str(testnum) + ';' + str(errnum) +'\n')


        return

    @staticmethod
    def read_data():
        daytime = time.strftime("%H",time.localtime(time.time()))
        if int(daytime) >=16 and int(daytime) <17:
            (page,table) = MailSender.generate_result_content()
            s =[]
            #f = open('C:\\Users\\liuxiumei\\PycharmProjects\\404\\result.txt')
            f = open('D:\\leshitest\\result.txt')

            line = f.readline()
            while line:
                tmp = line.split(";")
                s.append(tmp)
                line = f.readline()
            f.close()
            for i in range(len(s)):
                tr = MailSender.add_result_content(table,s[i][0], s[i][1], s[i][2], s[i][3], s[i][4])
                content = page.printOut()
            total = u'【前端自动化测试监测】 PC主站-404错误,总结报告'
            #MailSender.send_mail('liuxiumei@letv.com',['liuxiumei@letv.com'],total,content,[])
            MailSender.send_mail('songjie@letv.com',['songjie@letv.com','songjie@letv.com'],total,content,[])
            file = 'D:\\leshitest\\result.txt'
            #file = 'C:\\Users\\liuxiumei\\PycharmProjects\\404\\result.txt'
            if os.path.exists(file):
                     os.remove(file)


    @staticmethod
    def send_mail():
        channels = list(set([ link.channel for link in Worker.errlinks ]))
        recommends = Worker.recommendlinkdict.values()
        (page,table) = MailSender.generate_mail_primary()
        send = False
        for channel in channels:
            (page,table) = MailSender.generate_mail_primary()

            for link in Worker.errlinks:
                if link.text.find('[IMG]') == -1 and link.channel == channel:

                    #(page,table) = MailSender.generate_mail_primary()
                    channelname = MailSender.get_channelname(channel)
                    tr = MailSender.add_mail_item(table, channelname, channel, link.url, link.text, link.code)
                    send = True
                    # to = MailSender.get_send_to_address(channel)
                    # content = page.render()
                    # Test = u'【前端自动化测试监测】 PC主站-404错误报告'
                    # MailSender.send_mail('liuxiumei@letv.com',to,Test,content,[])


            if not  send:
                continue

            to = MailSender.get_send_to_address(channel)
            content = page.render()
            Test = u'【前端自动化测试监测】 PC主站-404错误报告'
            MailSender.send_mail('songjie@letv.com',to,Test,content,[])

        #按 推荐 发送报告
        (page1,table1) = MailSender.generate_mail_primary()
        send= False
        for url in recommends:
            for link in Worker.errlinks:

                if link.url == url:
                    tr = MailSender.add_mail_item(table, '推荐', channel, link.url, link.text, link.code)
                    send = True

        if send:
            content = page1.render()
            Test = u'【前端自动化测试监测】 PC主站-404错误报告'
            #MailSender.send_mail('liuxiumei@letv.com',['liuxiumei@letv.com'],'Test',content,[])
            #MailSender.send_mail('liuxiumei@letv.com',['liuxiumei@letv.com','chenjia6@letv.com','gaohaiyang@letv.com','wangjingfei@letv.com','wanglinhu@letv.com'],'Test',content,[])
