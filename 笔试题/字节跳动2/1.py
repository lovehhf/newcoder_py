# -*- coding:utf-8 -*-

__author__ = 'huanghf'

import sys

# for line in sys.stdin:
#     a = line.split()
#     M.append(a)
# M = list(map(lambda x:list(map(int,x)),M))


M = [['1', '2', '1'],
     ['1', '1', '0'],
     ['0', '1', '1']]

M = list(map(lambda x:list(map(int,x)),M))

def fun(M):
    r, c = len(M), len(M[0])

    coder = []
    for i in range(r):
        for j in range(c):
            if M[i][j] == 2:
                coder.append((i, j, 0))
    # print(coder)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0
    while coder:
        i, j, res = coder.pop(0)
        # 找到程序员身边的产品经理, 并感染
        for xd, yd in d:
            x = i + xd
            y = j + yd
            if 0 <= x < r and 0 <= y < c and M[x][y] == 1:
                M[x][y] = 2
                coder.append((x, y, res + 1))

    if any(1 in row for row in M):
        return -1
    return res

print(fun(M))