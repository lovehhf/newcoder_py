# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小明热衷于买足球彩票多年而苦苦不能中奖。经过他近日的潜心研究，小明发现了一个提高中奖几率的方法。
已知足球比赛有胜、负、平三种结果，小明的方法是，如果买一张含有n场比赛的彩票，那么相邻两场比赛的结果不能相同，且第一场比赛和最后一场比赛的结果也不能相同。
请你帮小明算算，符合条件的彩票有多少种


输入描述:
输入一个整数N（0<=N<=50)，表示比赛的场数

输出描述:
输出一个整数M，表示满足条件的情况数

输入例子1:
3

输出例子1:
6

eg：n=5,0:胜,1平:负
0
12
0201 -> 2*3
12011202 -> 6*3 
0201120202011201->10*3  16-6 因为最后的0不符合要求->10 10*3 = 30

类似于LeetCode 38. 报数

找规律

for i in range(len(dp)):
    print(i,dp[i].count(0),len(dp[i]))
    
0 1 1
1 0 2
2 2 4
3 2 8
4 6 16
5 10 32
6 22 64
7 42 128
8 86 256
9 170 512
10 342 1024
11 682 2048
12 1366 4096
13 2730 8192
14 5462 16384

dp[i] = 2**i-dp[i-1]
res = (2**i-dp[i])*3
"""

def solve(n):
    """
    2**i - dp[i-1] i-1行0的个数
    dp[i] 第i行中1,2的个数
    :param n:
    :return:
    """
    if n <= 1:
        return n * 3
    dp = [0]*n
    for i in range(1,n):
        dp[i] = 2**i - dp[i-1]
    res = dp[-1]*3
    # print(dp)
    # print(res)
    return res

def solve2(n):
    """
    内存超限 46.67%
    :param n:
    :return:
    """
    if n <= 1:
        return n * 3
    dp = [[] for _ in range(n)]
    dp[0] = [0]
    for i in range(1, n):
        for j in dp[i - 1]:
            t = [0, 1, 2]
            t.pop(j)
            dp[i] += t
    for i in range(len(dp)):
        print(i,dp[i].count(0),len(dp[i]))
    res = (dp[-1].count(1) + dp[-1].count(2)) * 3
    return res


def test():
    n = 15
    print(solve(n))
    print(solve2(n))


def main():
    n = int(input())
    print(solve(n))


test()
