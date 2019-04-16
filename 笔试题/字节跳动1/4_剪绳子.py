# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
有N根绳子，第i根绳子长度为Li，现在需要M根等长的绳子，你可以对N根绳子进行任意裁剪（不能拼接），请你帮忙计算出这M根绳子最长的长度是多少。

输入格式
第一行包含2个正整数N、M，表示原始绳子的数量和需求绳子的数量。

第二行包含N个整数，其中第 i 个整数Li表示第 i 根绳子的长度。

输出格式
输出一个数字，表示裁剪后最长的长度，保留两位小数。

数据范围
1≤N,M≤100000,
0<Li<10^9
输入样例：
3 4
3 5 4
输出样例：
2.50
样例解释
第一根和第三根分别裁剪出一根2.50长度的绳子，第二根剪成2根2.50长度的绳子，刚好4根。
"""

M,N = list(map(int,input().split(' ')))
L = list(map(int,input().split(' ')))

# # M原始绳子的数量,N:需要绳子的数量
# M,N = 3,4
# L = [3,5,4]

"""
30 40
59 40 46 65 16 24 96 50 80 58 30 50 18 59 4 20 11 20 24 21 50 87 20 61 30 59 22 80 17 20
标准答案
21.75
"""


def check(N,L,mid):
    """
    模拟剪绳子
    剪出绳子的数量等于需要绳子的数量，返回True
    :param M:
    :param N:
    :param L:
    :param mid:
    :return:
    """
    # print([x//mid for x in L])
    num = sum([x//mid for x in L])
    if num>=N:
        return True
    return False

def fun(M,N,L):
    L.sort()

    left = 0
    right = L[-1]
    while right-left>1e-6:
        mid = (left+right)/2
        if check(N,L,mid):
            left = mid
        else:
            right = mid
    return '%.2f'%left



print(fun(M,N,L))