#coding=utf-8
from email.mime.text import MIMEText
import os
from htds_interface_agin_test.common.read_config_file import ConfigFile,pro_path
import smtplib
def send_email(report_file):
    cf = ConfigFile()
    report_name = os.path.join(pro_path,"report",report_file)
    with open(report_name,"rb") as f:
        body = f.read()
    #邮件发送的内容
    msg = MIMEText(body,"utf-8","html")
    #邮件主题
    msg["subject"] = cf.get_email("subject")
    #发件人
    msg["From"] = cf.get_email("user")
    #收件人
    msg["To"] = cf.get_email("receiver")
    #smtpib.SMTP() 实例化
    smtp = smtplib.SMTP()
    #连接邮件服务器
    smtp.connect(cf.get_email("server"))
    #登录邮箱
    smtp.login(cf.get_email("user"),cf.get_email("passwd"))
    #发送邮件
    smtp.sendmail(cf.get_email("user"),cf.get_email("receiver"),msg.as_string())
    print("邮件发送成功")
if __name__ == '__main__':
    send_email("report.html")
