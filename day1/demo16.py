#!/usr/bin/env python
# coding=utf-8
#学习字典和函数的配合
import random#模块引入
def add(a,b):
    return a+b

def div(a,b):
    if a > b:
        return a-b
    else:
        return b-a

a = random.randint(1,10)
b = random.randint(1,10)
c = random.choice(("+","-"))
print("a=%d"%a)
print("b=%d"%b)
print("c=%s"%c)
cal = {"+":add,"-":div}
print(cal[c])#cal[c]就是div或者add
#div(a,b)
s = cal[c](a,b)

print("%d %s %d = %d"%(a,c,b,s))
#%s对应的是字符串
#%d对应的是整数
name = "tom"
age = 22
b = "my name is %s,my old is %d"%(name,age)
print(b)
