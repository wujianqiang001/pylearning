# -*- coding:utf-8 -*-
'''
请求接口,问题：什么情况用params 、data、json
'''
import requests,json,logging,os
from APITest.util.tools import *

ticket = readConfig("config/config.ini","ticket","ticket")

def request_get(url,header,body):
    # url = "http://lebz-api.le.com/backend/AccountManage/AccountList"
    # header = {"ticket":ticket}
    # body = {"search_uid":"30655","search_order_status":"success","search_payment_type":"1"}
    response = requests.get(url,headers = header,params = body)
    return json.loads(response.text)

# def request_get():
#     url = "http://lebz-api.le.com/backend/AccountManage/AccountList"
#     header = {"ticket":ticket}
#     body = {"search_uid":"30655","search_order_status":"success","search_payment_type":"1"}
#     response = requests.get(url,headers = header,params = body)
#     return response.text

# def request_post():
#     url = "http://lebz-api.le.com/backend/mallManage/AddCategoryInfo"
#     header = {"Content-Type":"application/x-www-form-urlencoded","ticket" :ticket}
#     body = {"category_name":"20180703-4","weight":105,"map_name":"帽子"}
#     response = requests.post(url,headers = header,data = body)
#     return response.text


if __name__ == "__main__":
    response = request_get("http://lebz-api.le.com/backend/AccountManage/AccountList",{"ticket":ticket},{"search_uid":"30655","search_order_status":"success","search_payment_type":"1"})
    #print(type({"search_uid":"30655","search_order_status":"success","search_payment_type":"1"}))
    print(response)
    #print(type(response))
    logging.basicConfig(filename=os.path.join(os.getcwd(),'../log/log.txt'),level=logging.DEBUG)
    logging.debug('this is a message')
    print("---------------")