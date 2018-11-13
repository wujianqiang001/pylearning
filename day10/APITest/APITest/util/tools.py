# -*- coding:utf-8 -*-
from configparser import ConfigParser

#读取配置文件
def readConfig(FPath,lable1,lable2):
    conf = ConfigParser()
    conf.read(FPath)
    value = conf.get(lable1,lable2)
    return value


if __name__ == "__main__":
    value = readConfig("../config/config.ini","excel","address")
    print(value)