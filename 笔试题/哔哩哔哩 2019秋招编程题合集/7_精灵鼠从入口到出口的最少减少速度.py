# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：2秒
空间限制：131072K

猛兽侠中精灵鼠在利剑飞船的追逐下逃到一个n*n的建筑群中，精灵鼠从（0,0）的位置进入建筑群，建筑群的出口位置为（n-1,n-1）
建筑群的每个位置都有阻碍，每个位置上都会相当于给了精灵鼠一个固定值减速，因为精灵鼠正在逃命所以不能回头只能向前或者向下逃跑
现在问精灵鼠最少在减速多少的情况下逃出迷宫？

输入描述:
第一行迷宫的大小: n >=2 & n <= 10000；
第2到n+1行，每行输入为以','分割的该位置的减速,减速f >=1 & f < 10。

输出描述:
精灵鼠从入口到出口的最少减少速度？

输入例子1:
3
5,5,7
6,7,8
2,2,4

输出例子1:
19
"""


def solve(n, matrix):
    dp = [[0] * n for _ in range(n)]
    dp[-1][-1] = matrix[-1][-1]
    for i in range(n - 2, -1, -1):
        dp[-1][i] = matrix[-1][i] + dp[-1][i + 1]
    for i in range(n - 2, -1, -1):
        dp[i][-1] = matrix[i][-1] + dp[i + 1][-1]
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + matrix[i][j]
    return dp[0][0]


matrix = []
n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input().split(','))))
res = solve(n, matrix)
print(res)
