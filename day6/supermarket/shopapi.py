#!/usr/bin/env python
# coding=utf-8
from flask import Flask,jsonify,request
app = Flask(__name__)
def getdata():
    trades = {}
    with open("trades.txt") as f:
        for line in f:
            line = line.strip()
            ts = line.split("|")
            trades[ts[0]] = round(float(ts[1]),2)
    return trades

def gettradedata():
    with open("trades.txt") as f:
        trades = f.readlines()
    return trades

def writetrades(trades):
    with open("trades.txt","w") as f:
        f.writelines(trades)

@app.route("/",methods=["GET","POST"])
def index():
    return "hello world"
@app.route("/gettrades",methods=["GET","POST"])
def gettrades():
    data = getdata()
    trades = data.keys()
    return jsonify(list(trades))
@app.route("/gettprice",methods=["GET","POST"])
def gettprice():
    data = getdata()
    trade = request.args.get("trade")
    price = data.get(trade)
    return str(price)

@app.route("/gettprices",methods=["GET","POST"])
def gettprices():
    data = getdata()
    trade = request.args.get("trade")
    if trade in data.keys():
        price = request.args.get("price")
        unit = request.args.get("unit")
        print(unit)
        return str(round(float(price)*int(unit),2))
    else:
        return "this trade is not exist!"

@app.route("/addtrade",methods=["GET","POST"])
def addtrade():
    trade = request.args.get("trade")
    price = request.args.get("price")
    trades = gettradedata()
    for t in trades:
        if trade in t:
            return "{} is exits!".format(trade)
    else:
        trades.append("{}|{}\n".format(trade,price))
        writetrades(trades)
        return "addtrade success"

@app.route("/deletetrade",methods=["GET","POST"])
def deletetrade():
    trade = request.args.get("trade")
    trades = gettradedata()
    for t in trades:
        if trade in t:
            trades.remove(t)
    writetrades(trades)
    return "delete {} success".format(trade)

@app.route("/updatetrade",methods=["GET","POST"])
def updatetrade():
    trade = request.args.get("trade")
    price = request.args.get("price")
    trades = gettradedata()
    for t in trades:
        if trade in t:
            trades[trades.index(t)] = "{}|{}\n".format(trade,price)
    writetrades(trades)
    return "update {} success".format(trade)

if __name__ == "__main__":
    app.run()