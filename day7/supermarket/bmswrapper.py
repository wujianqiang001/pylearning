#!/usr/bin/env python
# coding=utf-8
def gettrades():
    with open("trades.txt") as f:
        trades = f.readlines()
    return trades

def writetrades(trades):
    with open("trades.txt","w") as f:
        f.writelines(trades)

def addtrade(trade,price):
    trades = gettrades()
    for t in trades:
        if trade in t:
            pass
    else:
        trades.append("{}|{}\n".format(trade,price))
        writetrades(trades)

def deletetrade(trade):
    trades = gettrades()
    for t in trades:
        if trade in t:
            trades.remove(t)
    writetrades(trades)

def updatetrade(trade,price):
    trades = gettrades()
    for t in trades:
        if trade in t:
            trades[trades.index(t)] = "{}|{}\n".format(trade,price)
    writetrades(trades)

if __name__ == "__main__":
    updatetrade("pear",3.50)