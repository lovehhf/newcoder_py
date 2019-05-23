# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
有两个用字符串表示的非常大的大整数,算出他们的乘积，也是用字符串表示。不能用系统自带的大整数类型。
输入描述:
空格分隔的两个字符串，代表输入的两个大整数
输出描述:
输入的乘积，用字符串表示

输入
72106547548473106236 982161082972751393
输出
70820244829634538040848656466105986748

11
11
---
011
11
---
121
"""


def solve(A, B):
    m, n = len(A), len(B)
    res = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            a, b = int(A[i]), int(B[j])
            x, y = a * b // 10, a * b % 10
            res[i+j + 1] += y
            res[i+j] += x
    # print(res)
    for i in range(m+n-1,0,-1):
        carry,r = res[i]//10,res[i]%10
        res[i-1] += carry
        res[i] = r
    # print(res)
    res = ''.join([str(x) for x in res]).lstrip('0')
    return res


def main():
    A, B = input().split()
    print(solve(A, B))


def test():
    A, B = '72106547548473106236', '982161082972751393'
    print(solve(A, B))


test()
