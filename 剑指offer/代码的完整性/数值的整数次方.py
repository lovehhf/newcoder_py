# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


class Solution:

    def Power(self, base, exponent):
        p = abs(exponent)
        r = 1.0
        while p:
            if p & 1:
                r *= base
            base *= base
            p >>= 1
        return 1 / r if exponent < 0 else r

    def Power_2(self, base, exponent):
        return base ** exponent


base, exponent = 2.5, 3
s = Solution()
print(s.Power(base, exponent))
