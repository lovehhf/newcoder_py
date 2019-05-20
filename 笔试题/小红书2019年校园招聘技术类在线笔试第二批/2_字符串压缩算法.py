# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一串字符，请编写一个字符串压缩程序，将字符串中连续出现的重复字母进行压缩，并输出压缩后的字符串。
例如：
aac 压缩为 1ac
xxxxyyyyyyzbbb 压缩为 3x5yz2b


输入描述:
任意长度字符串

输出描述:
压缩后的字符串

输入例子1:
xxxxyyyyyyzbbb

输出例子1:
3x5yz2b
"""


def solve(s):
    s = s + '0'
    L, R = 0, 1
    res = ''
    n = len(s)
    while R < n:
        if s[L] == s[R]:
            R += 1
        else:
            res += str(R - L - 1) + s[L] if R - L > 1 else s[L]
            L = R
            R += 1
    return res


s = "xxxxyyyyyyzbbb"
print(solve(s))
