#!/usr/bin/env python
# coding=utf-8
import string, random, json, copy
a = string.ascii_lowercase
b = string.digits
c = a + b
D = {"version":123456,"add_domains":
    [{"1fdix.1bka.axy1.com":{"host":"1fdix.1bka.axy1.com","preproy":"switch","TLL":0}},
     {"rus1f.07hf.2xms.com":{"host":"rus1f.07hf.2xms.com","preproy":"switch","TLL":1}},
     {"cqphe.r7mw.nh6u.com":{"host":"cqphe.r7mw.nh6u.com","preproy":"switch","TLL":2}},
     {"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}},
     ]}
count0 = D["add_domains"][-1] #获取字典D中add_domains对应值的最后一个元素，因为add_domains对应的值是一个列表
                              #也就是说：D["add_domais"]是一个列表
count1 = list(count0.values())[0] #count0是一个字典，
                                  #即：{"sz8al.d69n.2b6o.com":{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}
                                  #获取字典count0内的值，python3是dict_values类型，所以需要转换成列表类型，才可以取值
                                  #因为count0内的value值只有一个，所以使用下标0
                                  
count = count1["TLL"] #count1是{"host":"sz8al.d69n.2b6o.com","preproy":"switch","TLL":3}
                      #count的值就是3
                      #通过以上3步，就可以获取原始数据最大的TLL值
#以上3步，也可以一步实现：count = list(D["add_domains"][-1].values())[0]["TLL"]                     
for i in range(10):
    L = []
    for i in range(3):
        if i == 0:
            L.append("".join(random.sample(c, 5)))#random.sample(c, 5)随机函数，从c中随机取5个值，返回列表类型，通过join把列表内容拼接
        else:
            L.append("".join(random.sample(c, 4)))
    L.append("com")
    host = ".".join(L)
    count += 1 #每次循环，count自增1，即count = count + 1,简写为：count += 1
    sv = copy.copy(D["add_domains"][0]["1fdix.1bka.axy1.com"]) #通过copy浅拷贝，不改变D原始数据的内容
                                                              #可以通过该例子理解copy.copy的用法
                                                              #a = {"a": "A"}
                                                              #b = a
                                                              #b["a"] = "B"
                                                              #这样的结果是，a和b都是{"a":"B"}
                                                              #如果引入copy模块
                                                              #import copy
                                                              #a = {"a": "A"}
                                                              #b = a
                                                              #b["a"] = "B"
                                                              #这样的结果是：a是{"a":"A"},b是{"a":"B"}
    sv["host"] = host #从最里层开始更新内容
    sv["TLL"] = count #同理
    D["add_domains"].append({host:sv})#因为D["add_domains"]是一个列表，通过append追加新字典，键是新生成的host,对应值是sv
print (D)
for s in D["add_domains"]:
    print (s)
