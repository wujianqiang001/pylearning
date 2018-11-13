#!/usr/bin/env python
# coding=utf-8
from Day2.lianxi5 import *

rate = 1
name = "xiaoming"
region = "beijing"
trades = {}
#商品的数量
counts = 3
sum=0

print("欢迎前来购物\n")
def er(counts,sum):
    count = 0
    with open("price")as f:
        for _trade in f:
            trade = _trade.strip().split("|")
            trades[trade[0]] = trade[1]
            print("商品信息：" + "一斤" + str(trade))
            # print(trades)
    m = input("请输入您购买的商品\n")
    for key in trades:
        if m == key:
            trade = m
            break
        else:
            count += 1
            if count == counts:
                print("请输入已有的商品")
                er(counts,sum)
            else:
                pass

    n = input("请输入您购买的斤数\n")
    s = int(n)
    print("此商品的总价格是" + str(sumprice(trade, s, rate)))
    a = input("是否购买---是输入‘Y’,否输入'N'\n")

    if a == "Y".lower()[0]:
        print("订单=" + order(trade, name, region, rate))
        print("此商品的总价格是" + str(sumprice(trade, s, rate)))
        write(trade, name, region, s, rate)
    else:
        print("欢迎下次光临")
        exit(0)
    b = input("是否继续购买---是输入‘Y’,否输入'N'\n")
    if b == "Y".lower()[0]:
        er(counts,sum)
    else:
        print("欢迎下次光临")
        exit(0)
#er(counts,sum)








