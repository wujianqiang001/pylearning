import requests,json,re
from api.com.check import *
def request(method,url,body,expection):
    if method == "get":
        r = requests.get(url,params=body)
        try:
            content = r.json()
            check_pytest(expection,content)
        except:
            content = r.text
            url = re.findall("href=\"(.+?)\"",content)[0]
            r = requests.get(url)
            content = r.json()
            print(type(content))
            check_pytest(expection,content)
        return r
    if  method == "post":
        cookies = {"PublicParam":"LoginUrl=http://221.123.191.53:8123/#","ASP.NET_SessionId":"pmteck01ngbvrny31ktc4xtz"}
        r = requests.post(url,data=body,cookies = cookies)
        try:
            content = r.json()
            check_pytest(expection, content)
        except:
            content = r.text
            check_pytest(expection,content)
        return r


