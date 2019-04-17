# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a,b = 1,2
        for i in range(number-1):
            a,b = b,a+b
        return a

number = 100
s = Solution()
print(s.rectCover(number))