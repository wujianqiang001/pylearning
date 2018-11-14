#!/usr/bin/env python
# coding=utf-8
#根据一句话的关键词，给该句话打标签
labels = {"美食":["吃","吃饭","小龙虾","海鲜","香蕉"],
          "旅游":["五台山","黄山"],
          "摄影":["拍照","对焦"]}

content = "晚上,在,黄山,吃,小龙虾,美味,！"
contents = content.split(",")
def getlabels(contents):
    for c in contents:
        for k,v in labels.items():
            if c in v:
                return k

def getlabels1(contents):
    dicts = {}
    for c in contents:
        for k,v in labels.items():
            if c in v:
                dicts[k] = c
    return tuple(dicts.keys())

def getlabels2(contents):
    dicts = {}
    for c in contents:
        for k,v in labels.items():
            if c in v:
                dicts[k] = c
                break
    return tuple(dicts.keys())
gl = getlabels2(contents)
print(gl)
#作业：优化该代码，可以给一句话打多个标签