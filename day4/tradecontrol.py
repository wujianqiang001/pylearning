#!/usr/bin/env python
# coding=utf-8
import os, json, time
def tradeget():
    with open("trades.txt") as f:
        trades = json.load(f)
    trade = []
    for t in trades:
        trade.append({"trade":t["trade"],"price":t["price"]})
    return trade

def tradepost(trade, price):
    with open("trades.txt") as f:
        trades = json.load(f)
    for t in trades:
        if t["trade"] == trade:
            return "This trade is exeits"
    t = trades[-1]
    NO = t["NO"]
    trades.append({"price":price,"trade":trade,"NO":NO+1,"updatetime":time.time()})
    with open("trades.txt", "w") as f:
        json.dump(trades, f)
    return "add trade success"

def tradeput(trade, price):
    with open("trades.txt") as f:
        trades = json.load(f)
    for t in trades:
        if t["trade"] == trade:
            t["price"] = price
            t["updatetime"] = time.time()
            with open("trades.txt", "w") as f:
                json.dump(trades, f)
            return "update trade success"
    return "This trade is exeits"

def tradedelete():
    pass

#print tradeget()
print tradeput("banana",4.90)
# print tradeget()
