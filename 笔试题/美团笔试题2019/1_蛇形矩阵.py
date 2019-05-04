# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入两个整数n和m，输出一个n行m列的矩阵，将数字 1 到 n*m 按照回字蛇形填充至矩阵中。

具体矩阵形式可参考样例。

输入格式
输入共一行，包含两个整数n和m。

输出格式
输出满足要求的矩阵。

矩阵占n行，每行包含m个空格隔开的整数。

数据范围
1≤n,m≤100
输入样例：
3 3
输出样例：
1 2 3
8 9 4
7 6 5
"""

# n行m列
n,m = list(map(int,input().split(' ')))
# n, m = 4, 3
res = [[0 for _ in range(m)] for _ in range(n)]

# 方向列表: 右下左上
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
c = 0  # 当前方向
i, j = 0, 0
cur = 1
while cur < m * n + 1:
    res[i][j] = cur
    dx, dy = d[c]
    # print(res)
    x, y = i + dx, j + dy  # 下一个需要填充的坐标
    # 需要转向的情况
    if x < 0 or x == n or y < 0 or y == m or res[x][y] != 0:
        c = (c + 1) % 4
        dx, dy = d[c]
        x, y = i + dx, j + dy
    i, j = x, y
    cur += 1

# print(res)
# for i in res:
for i in res:
    line = ' '.join([str(x) for x in i])
    print(line)