# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
一条直线上等距离放置了n台路由器。路由器自左向右从1到n编号。第i台路由器到第j台路由器的距离为|i-j|。  
每台路由器都有自己的信号强度，第i台路由器的信号强度为ai。
所有与第i台路由器距离不超过ai的路由器可以收到第i台路由器的信号（注意，每台路由器都能收到自己的信号）。
问一共有多少台路由器可以收到至少k台不同路由器的信号。

输入描述:
输入第一行两个数n , k（1≤n , k≤10^5）

第二行n个数, a1 , a2 , a3……… , an（0≤ai≤10^9）

输出描述:
输出一个数，一共有多少台路由器可以收到至少k台不同路由器的信号。

输入例子1:
4 4
3 3 3 3

输出例子1:
4
"""


def solve(n, k, nums):
    """
    暴力 33.33%
    :param n:
    :param k:
    :param nums:
    :return:
    """
    dp = [0] * n
    for i in range(n):
        d = nums[i]
        l = i - d if i > d else 0
        r = i + d if i + d < n else n - 1
        dp[l:r + 1] = [x + 1 for x in dp[l:r + 1]]
    res = [1 for x in dp if x >= k].count(1)
    print(res)


# n,k = list(map(int,input().split()))
# nums = list(map(int,input().split()))
n, k = 7, 4
nums = 3, 1, 3, 2, 3, 0, 3
solve(n, k, nums)
