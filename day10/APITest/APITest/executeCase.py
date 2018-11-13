# -*- coding:utf-8 -*-
'''
问题 1、不同的输入会有不用的返回结果，怎么验证 乱
     2、接口测试都应该验证哪些内容
     3、如果结果和我预期不一样，怎么调错
'''
from APITest.util.excelTools import *
from APITest.util.request import *
from APITest.util.log import *
from APITest.util.check import *
import logging,json
import pytest
address = readConfig("config/config.ini","excel","address")
    #ticket = readConfig("config/config.ini","ticket","ticket")
caseList = getCaseInfo(address)
@pytest.mark.parametrize("url,header,body,method,expect",caseList)
def test_main(url,header,body,method,expect):
    if header:
        header = json.loads(header)
    else:
        header = None
    if body:
        body = json.loads(body)
    else:
        body = None
    expect = json.loads(expect)
    response = request_get(method,url,header,body)
    check(response,expect)

if __name__ == "__main__":
    main()
