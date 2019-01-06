#!/usr/bin/env python
# coding=utf-8
import time
def getdata():
    trades = {}
    with open("trades.txt") as f:
        for line in f:
            line = line.strip()
            ts = line.split("|")
            trades[ts[0]] = round(float(ts[1]),2)
    return trades

def writedata(orderid):
    with open("orderid,txt","a") as f:
        f.write(orderid+"\n")
def gettrades():
    data = getdata()
    trades = data.keys()
    return list(trades)

def getprice(trade):
    data = getdata()
    trades = gettrades()
    if trade in trades:
        return data.get(trade)
    return None

def getprices(trade,s,rate=1):
    price = getprice(trade)
    if price:
        pricesum = price*s*rate
        return pricesum
    return None

def createorderid(trade,s):
    prices = getprices(trade,s)
    now = int(time.time())
    if prices:
        orderid = "%s%d%d"%(trade,prices*100,now)
        writedata(orderid)
        return orderid
    return 0

def goshopping():
    trades = gettrades()
    print("      \033[1;33;41m****welcome*****\033[0m")
    for t in trades:
        price = getprice(t)
        print("\033[1;31m%10s\033[0m:%10.2f"%(t,price))
    trade = input("\033[1;31mYou are going to buy that product:\n\033[0m")
    unit = input("\033[1;31mHow much do you plan to buy:\n\033[0m")
    prices = getprices(trade,int(unit))
    print("\033[1;31mYou need to pay:\033[0m   \033[1;33;41m%5.2f\033[0m"%prices)
    orderid = createorderid(trade,int(unit))
    print("\033[1;31mYour orderid is:%20s\n\033[0m"%orderid)

def main():
    flag = "Y"
    while flag == "Y":
        goshopping()
        flag = input("Do you want to continue buying? ")
        flag = flag[0].upper()
if __name__ == "__main__":
    main()