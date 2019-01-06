#!/usr/bin/env python
# coding=utf-8
import os,sys
import requests
import pyecharts
def delfile():
    path = "stocks/"
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)

def charts(content,stock,n):
    x = [int(content[i][0].strip()) for i in range(-n,-0)]
    y = [float(content[i][2].strip()) for i in range(-n,-0)]
    z = [int(content[i][-1].strip()) for i in range(-n,-0)]
    line = pyecharts.Line(stock)
    line1 = pyecharts.Line(stock)
    line.add("收盘价",x,y,legend_top="50%",legend_pos="80%",mark_line=["min","max"])
    line1.add("成交量",x,z,legend_top="50%",legend_pos="20%")
    grid = pyecharts.Grid(height=720,width=1200)
    grid.add(line,grid_bottom="60%",grid_left="10%")
    grid.add(line1,grid_top="60%",grid_right="10%")
    grid.render("stocks/{}.html".format(stock))

def getstock(stock,n):
    try:
        r = requests.get("http://data.gtimg.cn/flashdata/hushen/latest/daily/{}.js?maxage=43201&visitDstTime=1".format(stock))
        if r.status_code != 200:
            return
    except:
        return
    content = r.text
    content = content.split("\\n\\")
    content = content[2:-1]
    content = [c.split(" ") for c in content]
    # if float(content[-1][2]) > float(content[-2][2]) > float(content[-3][2]) and int(content[-1][-1]) > int(content[-2][-1]) > int(content[-3][-1]):
    if float(content[-1][2]) > float(content[-2][2]) > float(content[-3][2]):
        charts(content,stock,n)
        # sys.exit()
if __name__ == "__main__":
    stocks = []
    delfile()
    with open("zz1000.txt") as f:
        for line in f:
            if line.startswith("6"):
                line = "sh"+line
            else:
                line = "sz"+line
            stocks.append(line.strip())
    for s in stocks:
        getstock(s,30)