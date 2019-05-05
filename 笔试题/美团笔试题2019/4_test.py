# -*- coding:utf-8 -*-

__author__ = 'huanghf'

n = 10
grid = [[-1, 0, -1, 2], [-10, 6, -10, 3], [0, 4, 0, -3], [-4, 2, -4, 6], [-10, -6, -10, 6], [9, 5, 9, 7],
        [9, -1, 0, -1], [5, 2, 5, -7], [8, -1, -2, -1], [4, 7, 4, -7]]
s = set()
for x1, y1, x2, y2 in grid:
    if y1 == y2:
        a,b = min(x1,x2),max(x1,x2)
        for i in range(a,b+1):
            s.add((i,y1))
    if x1 == x2:
        a,b = min(y1,y2),max(y1,y2)
        for i in range(a,b+1):
            s.add((x1,i))

print(len(s))