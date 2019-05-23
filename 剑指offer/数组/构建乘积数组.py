# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""


class Solution:
    def multiply(self, A):
        """
        前缀积和后缀积
        pre_mul[i]:前i-1个的数的前缀积
        suff_mul[i+1]:后i-1的数的后缀积
        :param A:
        :return:
        """
        n = len(A)
        pre_mul, suff_mul = [1] * n, [1] * n
        for i in range(1, n):
            pre_mul[i] = pre_mul[i - 1] * A[i - 1]
            suff_mul[n - i - 1] = suff_mul[n - i] * A[n - i]
        return [pre_mul[i] * suff_mul[i] for i in range(n)]


nums = [1, 2, 3, 4, 5]
s = Solution()
print(s.multiply(nums))
