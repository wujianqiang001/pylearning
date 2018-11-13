#!/usr/bin/env python
# coding=utf-8
import random
def play(n):
    count = 0
    for i in range((n-1)*10+1,n*10+1):
        a = random.randint(1,n*10-1)
        b = random.randint(1,n*10-1)
        d = random.choice(["+","-"])
        if d == "+":
            c = input("%d+%d="%(a,b))
            m = True if c == str(a+b) else False
        else:
            if a > b:
                c = input("%d-%d="%(a,b))
                m = True if c == str(a-b) else False
            else:
                c = input("%d-%d="%(b,a))
                m = True if c == str(b-a) else False
        if m:
            print (u"√")
            count += 1
        else:
            print (u"×")
    if count >= 9:
        print (u"第%d关闯关成功"%n)
        return True
    else:
        print (u"第%d关闯关失败"%n)
        return False

flag = "Y"
while flag == "Y":
    for j in range(1,11):
        print (u"第%d关闯关开始"%j)
        print (u"%d以内数字相加减，共10题，答对9道，闯关成功，进入下一关！"%(j*10))
        if not play(j):
            flag = input(u"是否继续玩，继续请输入Y,否则输入N结束游戏！")
            break
