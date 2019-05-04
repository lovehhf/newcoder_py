# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小Q打算穿越怪兽谷，他不会打怪，但是他有钱。
他知道，只要给怪兽一定的金币，怪兽就会一直护送着他出谷。
在谷中，他会依次遇见N只怪兽，每只怪兽都有自己的武力值和要“贿赂”它所需的金币数。
如果小Q没有“贿赂”某只怪兽，而这只怪兽“武力值”又大于护送他的怪兽武力之和，这只怪兽就会攻击他。
小Q想知道，要想成功穿越怪兽谷而不被攻击，他最少要准备多少金币。


输入格式
第一行包含整数N，表示怪兽的数量。
第二行包含N个整数d1,d2,…,dn，表示每只怪兽的武力值。
第三行包含N个整数p1,p2,…,pn，表示收买N只怪兽所需的金币数。

输出格式
输出一个整数，表示所需最小金币数。

数据范围
1≤N≤50,
1≤di≤10^//;////12,
1≤pi≤2
输入样例1：
3
8 5 10
1 1 2
输出样例1：
2

输入样例2：
4
1 2 4 8
1 2 1 2
输出样例2：
6
"""


def fun(n, nums1, nums2):
    """
    dp:
    f(i,j) 表示顺利走完前i个怪兽，花j个金币，战斗力之和的最大值。

    # f[i][j] 顺利走完前i个怪兽，花j个金币，战斗力和的最大值
    # f[i][j] 有两种情况
    # 1. 贿赂第i个怪兽 f[i][j] = f[i-1][j-pi] + di
    # 2. 不贿赂第i个怪兽 f[i][j] =f[i-1][j]
    :param n:
    :param nums1:
    :param nums2:
    :return:
    """
    f = [[-1] * (n * 2 + 1) for i in range(n + 1)]
    f[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, 2 * n + 1):
            if j >= nums2[i - 1] and f[i - 1][j - nums2[i - 1]] != -1:
                # 贿赂
                f[i][j] = f[i - 1][j - nums2[i - 1]] + nums1[i - 1]
            if f[i - 1][j] >= nums1[i - 1]:
                # 不贿赂
                f[i][j] = max(f[i - 1][j], f[i][j])

    for i in f:
        print(i)
    res = 0
    for j in range(1, 2 * n + 1):
        if f[n][j] != -1:
            res = j
            break
    return res


n = int(input())
nums1 = [int(x) for x in input().split(' ')]
nums2 = [int(x) for x in input().split(' ')]

# n = 4
# nums1 = [2, 1, 1, 8]
# nums2 = [1, 2, 1, 2]

print(fun(n, nums1, nums2))
