#!/usr/bin/env python
# coding=utf-8
import re,json
def f1():
    g = '[08/Dec/2016:09:01:54 +0800] ...0.001 ...[222.72.2.47, 10.180.226.167] ...200 ...GET ...http://api.membership.levp.go.le.com/backend-act-msg/act/servertime?_callback=jQuery110104935861921403557_1481158914353&vipcsrf=158914664M&_=1481158914354 ...HTTP/1.1 ...292 ...DIRECT/127.0.0.1:9000 ...application/javascript;charset=UTF-8 ..."http://minisite.le.com/msite/payUserCenterM/main/index.shtml?ref=wdhyzx_m" ..."Mozilla/5.0 (Linux; Android 5.1.1; vivo V3Max A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 LetvMobileClient_126_android" ..."10266aa056CZcom2bZUqcviyGUWuqJcv87phWvROIdW2j4Lhd2P90Nlm34jSCevaUWPgAKIcXA,135051374" ...0.001 ...200 ...-'

    glog = g.split(" ...")
    ua = glog[11]
    print(ua)
    u = re.search("\d; (.+?) Build",ua)
    if u:
        print(u.groups()[0])
    ip = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})",g)
    print(ip)

def f2():
    g = '[08/Dec/2016:10:27:06 +0800] 0.061 [113.135.61.70, 10.180.226.24] 200 GET http://api.membership.levp.go.le.com/backend-act-user-info/act/user/albumInfo/videoList?_callback=jQuery110103835470868261255_1481164025120&vipcsrf=164025137A&id=10031884&platform=upload&pageNo=1&pageSize=60&_=1481164025122 HTTP/1.1 53058 DIRECT/127.0.0.1:9000 application/javascript;charset=UTF-8 "http://minisite.le.com/msite/mzVipAct/payNonageM/index.shtml" "Mozilla/5.0 (Linux; Android 6.0; EVA-TL00 Build/HUAWEIEVA-TL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Mobile Safari/537.36; 360 Aphone Browser (6.9.9.25cmcc)" "-,-" 0.061 200 -'
    # g = '[08/Dec/2016:16:16:14 +0800] 0.001 [112.99.95.61, 10.180.226.30] 200 GET http://api.membership.levp.go.le.com/backend-act-msg/act/servertime?_callback=jQuery1101028109765867702663_1481184973232&vipcsrf=184974015B&_=1481184973233 HTTP/1.1 293 DIRECT/127.0.0.1:9000 application/javascript;charset=UTF-8 "http://minisite.le.com/msite/mzVipAct/paycooperate/paycooperateact/index.shtml?ref=xbxwzb" "Mozilla/5.0 (Linux; Android 5.1.1; SM-N9109W Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 LetvMobileClient_126_android" "10273d4452haVWm1ITFfPa0VzcpcXZL4TZC17WscCnPEuKAG6pm1MXEm12YzhsjvxU0voiyT2OQ,145942717" 0.001 200 -'
    # g = '[08/Dec/2016:22:01:12 +0800] 0.002 [1.85.108.20, 10.180.226.166] 200 GET http://api.membership.levp.go.le.com/backend-act-msg/act/servertime?_callback=jQuery11010443641044665128_1481205671815&vipcsrf=205672158O&_=1481205671816 HTTP/1.1 291 DIRECT/127.0.0.1:9000 application/javascript;charset=UTF-8 "http://minisite.le.com/msite/payUserCenterM/main/index.shtml?ref=wdhyzx_m" "Mozilla/5.0 (Linux; Android 5.1.1; M623C Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 LetvMobileClient_126_android" "102c7a357a4hqean0lY148lkV0yqGULm2J9BjGAkXyuDTTdBrwqCtE0015cVUlt7g5q4Wm3OLA,223410658" 0.002 200 -'
    glog = g.split(" ")
    ua = " ".join(glog[13:-4])
    print(ua)
    u = re.search("\d; (.+?) Build",ua)
    if u:
        print(u.groups()[0])
def f3():
    g = r'[2018-08-01 17:52:22] , test.ljzxt ,  , INFO , 8012 , /home/work/wwwroot/open_platform/platform/Fund/LJZXT/Client.php:202 , request sys: {"serviceCode":"CFM0010001","version":"1.2","bizSerialNo":"20180801175222852","bizTimestamp":"20180801175222","orgNo":"10000009123234","authCode":"8472b8855590423b90f6b6b9bf63125f","param":"{\"contractNo\":\"ZD001\",\"orgBizNo\":1024586578456309760,\"productCode\":\"P103\",\"currency\":\"0\",\"reimburseCode\":\"2\",\"termUnit\":0,\"applyTerm\":3,\"applyAmount\":300000,\"loanDueDate\":\"20181015\",\"interestUnit\":2,\"applyInterest\":\"0.100000\",\"earlyDeductionRate\":\"0.0\",\"penaltyInterset\":\"0.0\",\"defaultPayRate\":\"0.0\",\"loanPurpose\":\"未知\",\"userMainInfo\":{\"orgUserNo\":\"340103196111091524\",\"userName\":\"张三\",\"idKind\":0,\"idNo\":\"340103196111091524\",\"mobileNo\":\"18100000000\",\"educationCode\":\"6\",\"address\":\"北京|东城区|鸿福路11号\",\"eMail\":\"\",\"qq\":\"\",\"maritalStatus\":8,\"userType\":\"13\",\"userNativePlace\":null,\"userBirthDate\":\"19611109\",\"industryType\":1,\"companyName\":\"dsfgsdfgsd\",\"companyAddress\":\"\",\"companyPhone\":\"\",\"jobYears\":5,\"userRelationInfo\":[]},\"userAccountInfo\":{\"collectAccType\":\"2\",\"collectAccName\":\"张三\",\"collectAccNo\":\"6226388000000095\",\"collectBankCode\":\"CMB\",\"collectBankName\":\"招商银行\",\"collectOpenBank\":\"华夏银行中关村大街支行\",\"repayAccType\":\"2\",\"repayAccName\":\"张三\",\"repayAccNo\":\"6226388000000095\",\"repayBankCode\":\"CMB\",\"repayBankName\":\"招商银行\",\"repayPhone\":\"18100000000\"},\"applyCollateralInfo\":[{\"orgCollateralNo\":\"FDY00003300\",\"collateralName\":\"房产\",\"collateralType\":\"3\",\"collateralIdKind\":\"13\",\"collateralIdNo\":\"yu872610109663\",\"houseBuildArea\":\"200.00\",\"houseLocation\":null,\"houseBuildYear\":\"20050714\",\"totalValue\":50000000,\"evaluationOrg\":\"微言\",\"evaluationDate\":\"20180801\",\"vcCollateralType\":\"2\",\"vcAssetType\":\"4\",\"vcBeginDate\":\"20050714\",\"vcEndDate\":\"20600616\",\"vcStartDate\":\"20180801\",\"vcVoucherEndDate\":\"20600616\"}],\"remark\":\"\",\"applyExtendInfo\":{\"baseMortgageRate\":\"0.010000\"}}","sign":"lRwWYxLB82Aookug6jxA0BjS5uamBNhClqn8XkVoSvKd81TnPvDQD+FsBkY+0LzcN0xvll+gmDpOzQHC2Fjnmqjc2bN0C20OZ9qUN\/JwM63eB\/yGJabAsXVRTYLEgK8zy7eCkiU1TzK3ApLfaqDzl6bpKmEN8goij\/iWZrVSo30="}'
    u = re.search("({.+})",g)
    if u:
        d = u.groups()[0]
    print(d)
    d = json.loads(d)
    print(d)
    print(json.loads(d["param"])["contractNo"])
f3()