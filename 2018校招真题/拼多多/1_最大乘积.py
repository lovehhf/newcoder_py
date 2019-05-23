# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)

输入描述:
无序整数数组A[n]

输出描述:
满足条件的最大乘积

示例1
输入
3 4 1 2
输出
24


1.没有负数: 最大的三个数
2.有负数: 三个数的最大乘机要么是最小的2个负数乘最大的1个正数,要么是最大的三个数的乘积
"""

import heapq

def solve2(n, nums):
    """
    直接排序，时间复杂度O(NlogN) 不符合要求
    :param n:
    :param nums:
    :return:
    """
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


def solve(n, nums):
    """
    求出最大的三个数a,b,c
    求出最小的2个数d,e
    时间复杂度O(n)
    :param n:
    :param nums:
    :return:
    """
    a,b,c = heapq.nlargest(3,nums)
    d,e = heapq.nsmallest(2,nums)
    return max(a*b*c,a*d*e)


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(solve(n, nums))


def test():
    n = 3
    nums = [1, 2, 3]
    print(solve(n, nums))


test()
