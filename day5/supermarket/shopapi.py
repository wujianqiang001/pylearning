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

if __name__ == "__main__":
    app.run()