# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个合法的表达式字符串，其中只包含非负整数、加法、减法以及乘法符号（不会有括号），例如7+3*4*5+2+4-3-1，请写程序计算该表达式的结果并输出；


输入描述:
输入有多行，每行是一个表达式，输入以END作为结束

输出描述:
每行表达式的计算结果

输入例子1:
7+3*4*5+2+4-3-1
2-3*1
END

输出例子1:
69
-1
"""

import sys

for line in sys.stdin:
    line = line.strip()
    if line!='END':
        print(eval(line))
