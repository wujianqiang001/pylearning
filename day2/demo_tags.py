#!/usr/bin/env python
# coding=utf-8
contents = "我,去,黄山,吃,小龙虾"
co = contents.split(",")
tags = {"美食":["吃","小龙虾"],
        "旅游":["黄山","五台山"]}

tag = {}
for c in co:
    for k,v in tags.items():
        if c in v:
            tag[k] = c

print(tag.keys())
