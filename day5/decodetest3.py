#!/usr/bin/env python
# coding=utf-8
import copy,datetime
from itertools import permutations
def timecount(fun):
    before = datetime.datetime.now()
    fun()
    end = datetime.datetime.now()
    print((end-before).total_seconds())

@timecount
def numsort1():
    print("bbbbbbbbbbbbbbbbbbbb")
    p = [1,2,3,4,5,6,7,8,9]
    s = permutations(p)
    for s1 in s:
        a1 = "".join([str(i) for i in s1[:4]])
        b1 = str(s1[4])
        c1 = "".join([str(i) for i in s1[5:]])
        if int(a1) * int(b1) == int(c1):
            print(a1,b1,c1)
@timecount
def numsort():
    print("aaaaaaaaaaaaaaaaa")
    p = [1,2,3,4,5,6,7,8,9]
    for i in p:
        q = copy.copy(p)
        q.remove(i)
        for j in q:
            t = copy.copy(q)
            t.remove(j)
            for k in t:
                s = copy.copy(t)
                s.remove(k)
                for l in s:
                    w = copy.copy(s)
                    w.remove(l)
                    for m in w:
                        x = copy.copy(w)
                        x.remove(m)
                        a = str(i)
                        b = "%d%d%d%d"%(j,k,l,m)
                        c = "".join([str(y) for y in x])
                        ab = sorted(str(int(a)*int(b)))
                        ac = sorted(c)
                        if ac == ab:
                            print(a,b,str(int(a)*int(b)))

numsort
numsort1

