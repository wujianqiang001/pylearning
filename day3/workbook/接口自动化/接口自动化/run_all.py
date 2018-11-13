#coding=utf-8
from common.send_email import send_email
import pytest
from common.read_config_file import ConfigFile,pro_path
import time,os
def main():
    cf = ConfigFile()
    t = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    report_dir = os.path.join(pro_path,cf.get_report("report_dir"))
    report_name = "report"+t+".html"
    pytest.main(["-q","testcase","--html="+os.path.join(report_dir,report_name)])
    send_email(report_name)
if __name__ == '__main__':
   main()




