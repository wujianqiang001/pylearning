# _*_ coding: UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import time
from pyh import *
import re
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
import os

errors = {10054:u'链接被重置',
          10060:u'链接超时',
          10061:u'链接被拒绝',
          0:u'发送有误',
          400:u'请求无效',
          403:u'禁止访问',
          404:u'无法找到文件',
          302:u'无法找到文件',
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

pathdir = os.path.join(os.getcwd(),'404')
channel_files = {'www':u'首页','tv':u'电视剧','movie':u'电影','comic':u'动漫','zongyi':u'综艺','ent':u'娱乐','life':u'生活','fun':u'搞笑','best':u'自制','music':u'音乐','edu':u'教育','tech':u'科技','qinzi':u'亲子','chuang':u'原创','auto':u'汽车','jilu':u'纪录片','travel':u'旅游','fashion':u'风尚','games':u'游戏','live':u'直播'}
#mails = {'www':['liuxiumei@letv.com'],'tv':['liuxiumei@letv.com'],'comic':['liuxiumei@letv.com'],'sports':['liuxiumei@letv.com'],'music':['liuxiumei@letv.com'],'ent':['liuxiumei@letv.com'],'zongyi':['liuxiumei@letv.com'],'movie':['liuxiumei@letv.com'],'finance':['liuxiumei@letv.com']}
#mails = {'girls':['sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhangluying@letv.com'],'games':['sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjinghan1@letv.com','gaolei@letv.com'],'ugc':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','sunjianhua1@letv.com','guofan@letv.com'],'fashion':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangying3@letv.com'],'pets':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangmeiyue1@letv.com'],'hot':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjinghan1@letv.com'],'travel':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangying3@letv.com'],'paike':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','chenxiang@letv.com'],'fun':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','chenxiang@letv.com'],'auto':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','yuanzhaoxin@letv.com'],'tech':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhangluying@letv.com'],'edu':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','liulu@letv.com'],'jilu':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','dongfang1@letv.com','wangpeng8@letv.com'],'qinzi':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','qiwen@letv.com','guogy@letv.com'],'news':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhoupengxiang@letv.com'],'best':['sihongjiang1@letv.com','wanglinhu@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhangyiao@letv.com'],'www':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','guanhui@letv.com','zhaofengliang@letv.com','xiedanqing@letv.com','baisen@letv.com','zhangsen@letv.com','yuchangjiang@letv.com','tangxq@letv.com','zhanghao@letv.com','wangying3@letv.com','zhangboyu@letv.com','wangyang@letv.com','lihaijun@letv.com','tengfei1@letv.com','wanglan@letv.com'],'tv':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjingfei@letv.com','wanglinhu@letv.com','mabingjie@letv.com','zoulei@letv.com','zhangpeng@letv.com','zhaofengliang@letv.com','wanglan@letv.com'],'comic':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjingfei@letv.com','wanglinhu@letv.com','mabingjie@letv.com','zoulei@letv.com','zhangpeng@letv.com','xiedanqing@letv.com','wanglan@letv.com'],'sports':['liuxiumei@letv.com','wangjingfei@letv.com','wanglinhu@letv.com','mabingjie@letv.com','baisen@letv.com','zhangsen@letv.com','zoulei@letv.com','zhangpeng@letv.com'],'music':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wanglinhu@letv.com','wangjingfei@letv.com','mabingjie@letv.com','zoulei@letv.com','zhangpeng@letv.com','zhanghao@letv.com','wanglan@letv.com'],'ent':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjingfei@letv.com','wanglinhu@letv.com','mabingjie@letv.com','zoulei@letv.com','zhangpeng@letv.com','yuchangjiang@letv.com','wanglan@letv.com'],'zongyi':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjingfei@letv.com','wanglinhu@letv.com','mabingjie@letv.com','zoulei@letv.com','zhangpeng@letv.com','tangxq@letv.com','wanglan@letv.com'],'movie':['sihongjiang1@letv.com','wangziwei1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjingfei@letv.com','wanglinhu@letv.com','mabingjie@letv.com','zoulei@letv.com','zhangpeng@letv.com','guanhui@letv.com','movie@letv.com','wanglan@letv.com'],'finance':['sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhangpeng@letv.com','wangyang@letv.com','wanglan@letv.com']}
#mails = {'girls':['zhangshu7@le.com','duanxiaolei@le.com','liuxiumei@letv.com','zhangluying@letv.com','songmeng@letv.com'],'games':['zhangshu7@le.com','duanxiaolei@le.com','lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjinghan1@letv.com','gaolei@letv.com'],'ugc':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','sunjianhua1@letv.com','guofan@letv.com'],'fashion':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangying3@letv.com'],'pets':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangmeiyue1@letv.com'],'hot':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangjinghan1@letv.com'],'travel':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangying3@letv.com'],'paike':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','chenxiang@letv.com'],'fun':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','chenxiang@letv.com'],'auto':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','yuanzhaoxin@letv.com'],'tech':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhangluying@letv.com'],'edu':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','liulu@letv.com'],'jilu':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','dongfang1@letv.com','wangpeng8@letv.com'],'qinzi':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','qiwen@letv.com','guogy@letv.com'],'news':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhoupengxiang@letv.com'],'best':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhangyiao@letv.com'],'www':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','guanhui@letv.com','zhaofengliang@letv.com','xiedanqing@letv.com','baisen@letv.com','zhangsen@letv.com','yuchangjiang@letv.com','tangxq@letv.com','zhanghao@letv.com','wangying3@letv.com','zhangboyu@letv.com','wangyang@letv.com','lihaijun@letv.com','tengfei1@letv.com','wanglan@letv.com'],'tv':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhaofengliang@letv.com','wanglan@letv.com'],'comic':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','xiedanqing@letv.com','wanglan@letv.com'],'sports':['lidong10@letv.com','liuxiumei@letv.com','baisen@letv.com','zhangsen@letv.com'],'music':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','zhanghao@letv.com','wanglan@letv.com'],'ent':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','yuchangjiang@letv.com','wanglan@letv.com'],'zongyi':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','tangxq@letv.com','wanglan@letv.com'],'movie':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','guanhui@letv.com','movie@letv.com','wanglan@letv.com'],'finance':['lidong10@letv.com','sihongjiang1@letv.com','liuxiumei@letv.com','chenjia6@letv.com','wangyang@letv.com','wanglan@letv.com']}
mails = {'www':['songjie@letv.com']}
#mails = {'live':['liuxiumei@letv.com'],'gongyi':['liuxiumei@letv.com'],'games':['liuxiumei@letv.com'],'ugc':['liuxiumei@letv.com'],'fashion':['liuxiumei@letv.com'],'yuanxian':['liuxiumei@letv.com'],'pets':['liuxiumei@letv.com'],'hot':['liuxiumei@letv.com'],'travel':['liuxiumei@letv.com'],'fun':['liuxiumei@letv.com'],'auto':['liuxiumei@letv.com'],'tech':['liuxiumei@letv.com'],'edu':['liuxiumei@letv.com'],'jilu':['liuxiumei@letv.com'],'qinzi':['liuxiumei@letv.com'],'news':['liuxiumei@letv.com'],'paike':['liuxiumei@letv.com'],'chuang':['liuxiumei@letv.com'],'best':['liuxiumei@letv.com'],'www':['liuxiumei@letv.com'],'tv':['liuxiumei@letv.com'],'comic':['liuxiumei@letv.com'],'sports':['liuxiumei@letv.com'],'music':['liuxiumei@letv.com'],'ent':['liuxiumei@letv.com'],'zongyi':['liuxiumei@letv.com'],'movie':['liuxiumei@letv.com'],'finance':['liuxiumei@letv.com']}
def get_file(channel,path=pathdir):
    assert isinstance(channel,str)
    assert os.path.isdir(path),'Argument path not existed'

    if channel == 'www':
        return os.path.join(path,'home.txt')

    return os.path.join(path,str(channel) + '.txt' )
    return os.path.join(path,str(channel) + '.txt' )

def get_channel(channelurl):
    name = '(\w*)\.le'
    ch1 = re.findall(name,channelurl)
    return ch1[0]

def get_channelname(channel):
    assert isinstance(channel,str)
    name = '(\w*)\.le'
    ch1 = re.findall(name,channel)
    return channel_files.get(ch1[0])

def get_send_to_address(channelurl):
    channel = get_channel(channelurl)
    if not mails.has_key(channel):
        raise RuntimeError('destination mail address not find')
    return mails[channel]

def get_send(channel):
    #assert isinstance(channel,str)
    return mails.get(channel)

#server['name'], server['user'], server['passwd']
def send_mail(fro, to, subject, text, files=[]):
    '''
    邮件发送
    @fro 发件人名称
    @to 收件人列表
    @subject 邮件标题
    @text 邮件正文
    @files 附件列表
    '''
    assert type(to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = 'liuxiumei@letv.com'
    msg['Subject'] = subject
    msg['To'] = COMMASPACE.join(to)  #COMMASPACE==', '
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text,'html','utf-8'))

    for file in files:
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data
        part.set_payload(open(file).read())
        #encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
        msg.attach(part)

    import smtplib
    smtp = smtplib.SMTP('smtp.letv.cn')
    smtp.ehlo()
    #smtp.starttls()
   # smtp.ehlo
    smtp.login('liuxiumei', 'Qwer')
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()
def generate_result_main(start_time,end_time,testname,testnum,errnum):
    page = PyH('reporter')
    page << h1('PC主站-404错误检测结果',c1='header1',style='color:black; text-align:center')
    table1 = page << table(border='1',id='mytable1',align='center',width="1500")
    headtr = table1 << tr(id='headline',c1='header1',style='color:white; text-align:center')
    headtr << td('开始时间',bgColor='#00FF00',width ='200',height ='30') << td('结束时间',bgColor='#00FF00',height ='30') << td('测试功能',bgColor='#00FF00',height ='30') << td('测试总数',bgColor='#00FF00',height ='30',width ='300') << td('404错误数',bgColor='#00FF00',height ='30',width ='300')
    trtemp = table1 << tr(id=str(uuid.uuid4()))
    trtemp << td(start_time) << td(end_time) << td(str(testname)) << td(str(testnum)) << td(errnum)

    return page.render()

def generate_result_content():
    page = PyH('reporter')
    page << h1('PC主站-404错误检测结果',c1='header1',style='color:black; text-align:center')
    table1 = page << table(border='1',id='mytable1',align='center',width="1500")
    headtr = table1 << tr(id='headline',c1='header1',style='color:white; text-align:center')
    headtr << td('开始时间',bgColor='#6da601',width ='200',height ='30') << td('结束时间',bgColor='#6da601',height ='30') << td('测试功能',bgColor='#6da601',height ='30') << td('测试总数',bgColor='#6da601',height ='30',width ='300') << td('404错误数',bgColor='#6da601',height ='30',width ='300')

    return (page,table1)

def add_result_content(table,start_time,end_time,testname,testnum,errnum):
   # trtemp = table << tr(id=str(uuid.uuid4()))
    trtemp = table << tr(id=('name'))
    trtemp << td(start_time) << td(end_time) << td(testname) << td(testnum) << td(errnum)

    return trtemp

def generate_mail_content(channelname,channel,url,urltext,urlcode):
    page = PyH('reporter')
    page << h1(u'PC主站-404错误检测结果',c1='header1',style='color:black; text-align:center')
    table1 = page << table(border='1',id='mytable1',align='center',width="1500")
    headtr = table1 << tr(id='headline',c1='header1',style='color:white; text-align:center')
    headtr << td('频道名称',bgColor='#FF6633',width ='200',height ='30') << td('频道url',bgColor='#FF6633',height ='30') << td('出错url地址',bgColor='#FF6633',height ='30') << td('出错url标题',bgColor='#FF6633',height ='30',width ='300') << td('错误码',bgColor='#FF6633',height ='30',width ='300')
    trtemp = table1 << tr(id=str(uuid.uuid4()))
    errtext = str(urlcode) + ' : ' + errors.get(int(urlcode))
    trtemp << td(channelname) << td(channel) << td(str(url)) << td(str(urltext)) << td(errtext)

    return page.printOut()

def generate_mail_primary():
    page = PyH('reporter')
    page << h1('PC主站-404错误检测结果',c1='header1',style='color:black; text-align:center')
    table1 = page << table(border='1',id='mytable1',align='center',width="1500")
    headtr = table1 << tr(id='headline',c1='header1',style='color:white; text-align:center')
    headtr << td('频道名称',bgColor='#FF6633',width ='200',height ='30') << td('频道url',bgColor='#FF6633',height ='30') << td('出错url地址',bgColor='#FF6633',height ='30') << td('出错url标题',bgColor='#FF6633',height ='30',width ='300') << td('错误码',bgColor='#FF6633',height ='30',width ='300')

    return (page,table1)

def add_mail_item(table,channelname,channel,url,urltext,urlcode):
    trtemp = table << tr(id=str(uuid.uuid4()))
    print urlcode
    errtext = str(404) + ' : ' + str(errors.get(int(urlcode)))
    print errtext
    trtemp << td(channelname) << td(channel) << td(url) << td(urltext) <<td(errtext)

    return trtemp



