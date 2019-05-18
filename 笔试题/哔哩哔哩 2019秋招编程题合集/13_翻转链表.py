# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：1秒
空间限制：32768K

对于一个链表 L: L0→L1→…→Ln-1→Ln,
将其翻转成 L0→Ln→L1→Ln-1→L2→Ln-2→…
输入是一串数字，请将其转换成单链表格式之后，再进行操作

输入描述:
一串数字，用逗号分隔

输出描述:
一串数字，用逗号分隔

输入例子1:
1,2,3,4,5

输出例子1:
1,5,2,4,3

1,2,3,4,5
"""


def solve(nums):
    n = len(nums)
    l, r = 0, n - 1
    res = []
    while l < r:
        res.append(nums[l])
        res.append(nums[r])
        l += 1
        r -= 1
    if l == r:
        res.append(nums[l])
    return ','.join([str(x) for x in res])


nums = input().split(',')
res = solve(nums)
print(res)
