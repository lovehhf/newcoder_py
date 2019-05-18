# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def solve(n, nums, k):
    i, res = 0, 0
    for j in range(n):
        if nums[j] == 0:
            k -= 1
        if (k < 0):
            if nums[i] == 0:
                k += 1
                i += 1
            else:
                while i < j and nums[i] == 1:
                    i += 1
                k += 1
                i += 1
        res = max(res, j - i + 1)
    print(res)


# n, k = 10, 2
# nums = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
solve(n, nums, k)
