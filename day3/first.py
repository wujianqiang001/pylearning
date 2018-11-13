#!/usr/bin/env python
# coding=utf-8
a = [[1,2,3,4,5],[2,3,4,5,6]]
b = [[1,2,33,4,5],[2,3,4,6,6]]
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] != b[i][j]:
            print a[i][j], b[i][j]

p = [(a[i][j],b[i][j]) for i in range(len(a)) for j in range(len(a[0])) if a[i][j] != b[i][j]]
print p
q = ((a[i][j],b[i][j]) for i in range(len(a)) for j in range(len(a[0])) if a[i][j] != b[i][j])
print q



a1 = [[1,2,3,4,5],[2,3,4,5,6]]
b1 = [[1,2,33,4,5],[2,3,4,6,6],[2,3,4,5,6],[2,3,4,5,6],[2,3,4,5,6]]
p = [(a1[i][j],b1[i][j]) for i in range(len(a1)) for j in range(len(a1[0])) if a1[i][j] != b1[i][j]]
p = [(a1[i][j],b1[i][j]) for i in range(len(a1)) for j in range(len(a1[0])) if a1[i][j] != b1[i][j]]
print p