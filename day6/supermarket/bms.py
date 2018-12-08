#!/usr/bin/env python
# coding=utf-8
def addtrade(trade,price):
    with open("trades.txt") as f:
        trades = f.readlines()
    for t in trades:
        if trade in t:
            pass
    else:
        trades.append("{}|{}\n".format(trade,price))
        with open("trades.txt","w") as f:
            f.writelines(trades)

def deletetrade(trade):
    with open("trades.txt") as f:
        trades = f.readlines()
    for t in trades:
        if trade in t:
            trades.remove(t)
    with open("trades.txt","w") as f:
        f.writelines(trades)

def updatetrade(trade,price):
    with open("trades.txt") as f:
        trades = f.readlines()
    for t in trades:
        if trade in t:
            trades[trades.index(t)] = "{}|{}\n".format(trade,price)
    with open("trades.txt","w") as f:
        f.writelines(trades)

if __name__ == "__main__":
    addtrade("pear",3.50)