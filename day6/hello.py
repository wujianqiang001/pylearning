#!/usr/bin/env python
# coding=utf-8
from flask import Flask,jsonify, request,abort, redirect,json
from day2 import shopping
app = Flask(__name__)

@app.route("/gettradeprice/<trade>")
def index(trade):
    price = shopping.tradeprice(trade)
    return "% s %.2f"%(trade, price)

@app.route("/gettradeprice1/<trade>")
def index1(trade):
    price = shopping.tradeprice_1(trade)
    return jsonify(price)
ua = {}
@app.route("/getua")
def getua():
    user_agent = request.headers.get("User_Agent")
    if ua.get(user_agent):
        ua[user_agent] += 1
    else:
        ua[user_agent] = 1
    if ua[user_agent] > 3:
        abort(405)
    else:
        return "<p> Your browser is %s</p>"%user_agent

@app.route("/return302")
def ret():
    return redirect("http://www.jd.com")

@app.route("/postrequest/",methods=["POST"])
def postrequest():
    print(request.data)
    p = json.loads(request.data)["trade"]
    price = json.loads(request.data)["price"]
    return jsonify({"trade":p,"price":price+1})

if __name__ == "__main__":
    app.run(debug=True,port=8801,host="0.0.0.0")