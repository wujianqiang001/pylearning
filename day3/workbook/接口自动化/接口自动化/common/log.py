#coding=utf-8
import logging
from htds_interface_agin_test.common.read_config_file import ConfigFile,pro_path
import os
import time
class Log():
    @classmethod
    def config_log(cls):
        #生成日志并设置日志等级
        cls.cf = ConfigFile()
        t = time.strftime("%Y%m%d%H_%M_%S",time.localtime(time.time()))
        log_dir = os.path.join(pro_path, cls.cf.get_log("log_dir"))
        log_path = os.path.join(log_dir,t+".log")
        cls.logger = logging.getLogger()
        cls.logger.setLevel(eval("logging."+cls.cf.get_log("log_level").upper()))
        #设置日志的句柄

        fh = logging.FileHandler(log_path,"a")
        sh = logging.StreamHandler()
        #设置日志输出格式
        ch = logging.Formatter("%(asctime)s - %(filename)s%[line:%(lineno)d] - %(levelname)s:%(message)s")
        #将日志句柄添加到日志中
        cls.logger.addHandler(fh)
        cls.logger.addHandler(sh)
    @classmethod
    def get_logger(cls):
        cls.config_log()
        return cls.logger
if __name__ == '__main__':
    log = Log()
    l = log.get_logger()
    l.info("苏珊珊")
    l.info("I LOVE YOU")
    l.info("8023")