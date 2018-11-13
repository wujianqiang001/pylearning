#!/usr/bin/env python
# coding=utf-8
from flask import Flask,request
import hashlib
app = Flask(__name__)

def getmd(value):
    md5 = hashlib.md5()
    md5.update(value.encode(encoding='utf-8'))
    signturn = md5.hexdigest()
    return signturn

@app.route("/getauth")
def index():
    t = request.args.get("t")
    auth = request.args.get("auth")
    key = "12345"
    signturn = getmd(t+key)
    print(signturn)
    if auth == signturn:
        return "hello"
    else:
        return "bad!"

if __name__ == "__main__":
    app.run()

