# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
公司的程序员不够用了，决定把产品经理都转变为程序员以解决开发时间长的问题。

在给定的矩形网格中，每个单元格可以有以下三个值之一：

值0代表空单元格;
值1代表产品经理;
值2代表程序员;
每分钟，任何与程序员(在4个正方向上)相邻的产品经理都会变成程序员。

返回直到单元格中没有产品经理为止所必须经过的最小分钟数。

如果不可能，返回-1。

以下是一个4分钟转变完成的示例：

2 1 1      2 2 1      2 2 2      2 2 2      2 2 2
1 1 0  ->  2 1 0  ->  2 2 0  ->  2 2 0  ->  2 2 0
0 1 1      0 1 1      0 1 1      0 2 1      0 2 2
输入格式
不固定多行（行数不超过10），毎行是按照空格分割的数字(不固定，毎行数字个数不超过10)。

其中每个数组项的取值仅为0、1、2三种。

读取时可以按行读取，直到读取到空行为止，再对读取的所有行做转换处理。

输出格式
如果能够将所有产品经理变成程序员，则输出最小的分钟数。

如果不能够将所有的产品经理变成程序员，则返回-1.

输入样例1：
0 2
1 0
输出样例1：
-1
输入样例2：
1 2 1
1 1 0
0 1 1
输出样例2：
3
输入样例3：
1 2
2 1
1 2
0 1
0 1
1 1
输出样例3：
4
"""

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