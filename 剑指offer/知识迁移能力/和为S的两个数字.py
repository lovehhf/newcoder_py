# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。

LeetCode 167. TwoSum2 
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        n = len(array)
        l, r = 0, n - 1
        while l < r:
            if array[l] + array[r] < tsum:
                l += 1
            elif array[l] + array[r] > tsum:
                r -= 1
            else:
                return array[l], array[r]
        return []


s = Solution()
print(s.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
