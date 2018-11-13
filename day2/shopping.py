#!/usr/bin/env python
# coding=utf-8
import time
def tradeprice(trade):
    with open("..\\day2\\trades.txt") as f:
        for _trade in f:
            trade_s = _trade.strip().split("|")
            if trade_s[0] == trade:
                return float(trade_s[1])
def gettrade():
    trades = []
    with open("trades.txt") as f:
        for t in f:
            trades.append(t.strip().split("|")[0])
    return trades

def tradeprice_1(trade):
    with open(r"..\day2\trades.txt") as f:
        trades = {}
        for _trade in f:
            trade_s = _trade.strip().split("|")
            trades[trade_s[0]] = float(trade_s[1])
    if trades.get(trade):
        return {"trade":trade,"price":trades[trade]}
    else:
        return {"trade":trade,"price":0}

def sumprice(trade, s, rate = 1):
    price = tradeprice_1(trade)
    sum_p = price * s * rate
    return sum_p

def orderid(trade, name, region):
    ts = int(time.time())
    return "%s%s%s%d"%(trade[0], name[0], region[0], ts)

def orders(trade, s, rate, name, region):
    price = tradeprice_1(trade)
    sum_ps = sumprice(trade, s, rate)
    order_id = orderid(trade, name, region)
    ts = int(order_id[3:])
    ts_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    return "|".join([order_id, trade, str(price), str(s), str(rate), str(sum_ps), name, region, ts_s])

def orderswrite(trade, s, rate, name, region):
    order_s = orders(trade, s, rate, name, region)
    with open("orders.txt", "a") as f:
        f.write(order_s + "\n")

# trade = "apple"
# name = "lily"
# region = "tianjin"
# s = 3
# rate = 0.95
# #print orders(trade, s, rate, name, region)
# #orderswrite(trade, s, rate, name, region)
# print gettrade()




