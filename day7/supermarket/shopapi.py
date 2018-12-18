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
    s = {"code":1000,"msg":"","data":list(trades)}
    return jsonify(s)

@app.route("/gettprice",methods=["GET","POST"])
def gettprice():
    data = getdata()
    trade = request.args.get("trade")
    price = data.get(trade)
    s = {"code":1000,"msg":"","data":str(price)}
    return jsonify(s)

@app.route("/gettprices",methods=["GET","POST"])
def gettprices():
    data = getdata()
    trade = request.args.get("trade")
    if trade in data.keys():
        price = request.args.get("price")
        unit = request.args.get("unit")
        s = {"code":1000,"msg":"","data":str(round(float(price)*int(unit),2))}
        return jsonify(s)
    else:
        return {"code":10001,"msg":"this trade is not exist!","data":[]}

@app.route("/addtrade",methods=["GET","POST"])
def addtrade():
    trade = request.args.get("trade")
    price = request.args.get("price")
    trades = gettradedata()
    for t in trades:
        if trade in t:
            s = {"code":10001,"msg":"{} is exits!".format(trade),"data":[]}
            return jsonify(s)
    else:
        trades.append("{}|{}\n".format(trade,price))
        writetrades(trades)
        s = {"code":10000,"msg":"addtrade success","data":[]}
        return jsonify(s)

@app.route("/deletetrade",methods=["GET","POST"])
def deletetrade():
    trade = request.args.get("trade")
    trades = gettradedata()
    for t in trades:
        if trade in t:
            trades.remove(t)
    writetrades(trades)
    s = {"code":10000,"msg":"delete {} success".format(trade),"data":[]}
    return jsonify(s)

@app.route("/updatetrade",methods=["GET","POST"])
def updatetrade():
    trade = request.args.get("trade")
    price = request.args.get("price")
    trades = gettradedata()
    for t in trades:
        if trade in t:
            trades[trades.index(t)] = "{}|{}\n".format(trade,price)
    writetrades(trades)
    s = {"code":10000,"msg":"update {} success".format(trade),"data":[]}
    return jsonify(s)

if __name__ == "__main__":
    app.run()