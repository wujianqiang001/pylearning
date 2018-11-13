#coding=utf-8
from configparser import ConfigParser
import os
pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class ConfigFile(object):
    def __init__(self,filename="config.conf"):
        self.cf = ConfigParser()
        self.cf.read(os.path.join(pro_path,"conf",filename))
    def get_server(self,option):
        return self.cf.get("server",option)
    def get_report(self,option):
        return self.cf.get("report",option)
    def get_email(self,option):
        return self.cf.get("email",option)
    def get_log(self,option):
        return self.cf.get("log",option)
if __name__ == '__main__':
    conf = ConfigFile()
    print(conf.get_report("report_dir"))

