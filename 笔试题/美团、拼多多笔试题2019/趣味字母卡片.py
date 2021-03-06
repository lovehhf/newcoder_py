# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小明给儿子小小明买了一套英文字母卡片（总共包含52张，区分大小写），小小明把卡片丢在地上玩耍，并从中取出若干张排成一排，形成了一个卡片序列。

此时，小明需要将卡片序列中的重复字母剔除（同一个字母的大小写只保留一个）。

请问，所有可能的结果中，字母序最小（不区分大小写）的序列的第一张卡片上是哪个字母？

输入格式
共一行，包含一个非空字符串，表示卡片序列，长度为N。

输出格式
共一行，包含一个字母（如果结果是大写字母，则需要转换成小写）。

数据范围
1≤N≤52
输入样例：
xaBXY
输出样例：
a
样例解释
剔除完后的结果是abxy。

[leetcode 316](https://leetcode.com/problems/remove-duplicate-letters/) 
"""

s = "zjRCDYxHgZAwiuVQkTyNeOpEXLbMdFGPqmJInBtUfvrohslWaKSc"
s = s.lower()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
# print(s)
# print(d)
stack = []
for i in s:
    if d[i] == 1:
        stack.append(i)
        break
    else:
        stack.append(i)
        d[i] -= 1

print(sorted(set(stack))[0])
