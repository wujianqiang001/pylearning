#!/usr/bin/env python
# coding=utf-8
import random
n = 1
def play(n):
    print(u"第%d关闯关开始"%n)
    print(u"%d以内数字相加减，共10题，答对9道，闯关成功，进入下一关！"%(n*10))
    count = 0
    for i in range((n-1)*10+1,n*10+1):
        nums = [random.randint(1,n*10-1) for i in range(2)]
        nums.sort(reverse=True)
        a,b = nums
        d = random.choice(["+","-"])
        if d == "+":
            c = input("%d+%d="%(a,b))
            m = True if c == str(a+b) else False
        else:
            c = input("%d-%d="%(a,b))
            m = True if c == str(a-b) else False
        if m:
            print(u"√")
            count += 1
        else:
            print(u"×")
    if count >= 9:
        print(u"第%d关闯关成功"%n)
        n += 1
        play(n)
    else:
        print(u"第%d关闯关失败"%n)
        flag = input(u"是否继续玩，继续请输入Y,否则输入N结束游戏！")
        if flag == "Y":
            play(1)
        else:
            return ""
play(n)