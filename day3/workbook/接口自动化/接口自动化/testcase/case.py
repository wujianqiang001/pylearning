#coding=utf8
from htds_interface_agin_test.common.read_config_file import ConfigFile
from htds_interface_agin_test.common.get_data import Data
import requests
from htds_interface_agin_test.common.log import Log
import json
class Case(object):
    def __init__(self):
        self.cf = ConfigFile()
        self.logger = Log.get_logger()
    def load_data(self,datafile):
        self.data = Data(datafile)
    def set_env(self,env):
        self.evn = env
    def run_case(self,sheetname,casename):
        case_data = self.data.ReadTestcase(sheetname,casename)
        url = self.cf.get_server(self.evn)
        data = case_data[3]
        data = json.loads(data)
        headers ={"Content-Type":"application/json"}
        if case_data[1].lower()=="post":
            resp = requests.post(url=url,json=data,headers=headers)
        else:
            resp = requests.get(url=url)
        return resp.text

    def log(self):
        return self.logger
if __name__ == '__main__':
    c=Case()
    c.set_env("url")
    c.load_data("interface_testcase.xlsx")
    r = c.run_case("login","test_login_normal")
    l = c.log()
    l.info(r)
