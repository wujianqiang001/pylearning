#!/usr/bin/env python
# coding=utf-8
#统计比赛得分，去掉一个最大值，去掉一个最小值，其它值的平均值，即该选手的成绩
#共10个裁判，满分为10分
#赋值的学习
score = [7,8.5,9.5,3,8.5,7.5,7.5,8.8,9.9,8.7]
score.sort()
print(score)
b,*middle,s = score#只针对python3,*middle
print(b)
print(middle)
print(s)
avgs = sum(middle)/len(middle)
print(avgs)