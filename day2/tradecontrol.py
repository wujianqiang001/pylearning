#!/usr/bin/env python
# coding=utf-8
import os
def tradeget():
    with open("trades.txt") as f:
        trades = {}
        for t in f:
            ts = t.strip().split("|")
            trades[ts[0]] = ts[1]
    return trades

def tradepost(trade, price):
    trades = tradeget()
    if trades.get(trade):
        pass
    else:
        with open("trades.txt", "a") as f:
            f.write("|".join([trade,str(price)])+"\n")

def tradeput(trade, price):
    trades = tradeget()
    if trades.get(trade):
        trades[trade] = str(price)
    else:
        pass
    with open("trades1.txt","a") as f:
        for k, v in trades.items():
            f.write("|".join([k,v])+"\n")
    os.remove("trades.txt")
    os.rename("trades1.txt", "trades.txt")


def tradedelete():
    pass

print tradeget()
tradeput("rice",3.90)
print tradeget()
