# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
import re

def NumberOf1(n):
    # write code here

    count = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        count += 1
        n = (n - 1) & n
    return count

print(NumberOf1(-255))