# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小镇沿街分布（可以理解为都在数轴上），有n家银行（位置以数轴的坐标表示，金额表示可以被抢走的金额）。
两个绑匪试图分别抢劫一个银行，为了让警方多奔波他们商定选择的两个银行距离不小于d。
请问，符合约定的情况下他们能抢到的总金额最大是多少。

输入格式
输入包含 n+1 行。

第一行包含两个整数 n 和 d，分别表示银行的数量和约定的距离。

接下来 n 行，每行包含两个整数 a 和 b ，分别表示坐标和金额。

输出格式
输出一个数字表示可以获得的最大金额。

数据范围
1≤n≤2∗105,
1≤d,a,b≤108
输入样例：
6 3
1 1
3 5
4 8
6 4
10 3
11 2
输出样例：
11
"""


def solve2(n, d, banks):
    """
    超时
    :param n:
    :param d:
    :param banks:
    :return:
    """
    banks = sorted(banks)
    res = 0
    for i in range(n):
        d1 = banks[i][0]
        j = i - 1
        k = i + 1
        while j >= 0 and d1 - banks[j][0] < d:
            j -= 1
        while k < n and banks[k][0] - d1 <= d:
            k += 1
        for x in banks[:j + 1] + banks[k:]:
            res = max(res, banks[i][1] + x[1])
    print(res)


def solve3(n, d, banks):
    """
    超时+1
    :param n:
    :param d:
    :param banks:
    :return:
    """
    banks = sorted(banks)
    res = 0
    for i in range(n):
        d1 = banks[i][0]
        k = i + 1
        while k < n and banks[k][0] - d1 < d:
            k += 1
        if banks[k:]:
            res = max(res, max([x[1] for x in banks[k:]]) + banks[i][1])
    print(res)


def solve(n, d, banks):
    """
    :param n:
    :param d:
    :param banks:
    :return:
    """
    banks = sorted(banks)
    res = 0
    j = 0
    maxv = 0
    for i in range(n):
        print(i, j, maxv, res)
        while j + 1 < i and banks[i][0] - banks[j + 1][0] >= d:
            j += 1
            maxv = max(maxv, banks[j][1])
        res = max(res, banks[i][1] + maxv)
    print(res)


def solve4(n, d, banks):
    """
    为啥这也行?!好像有bug
    :param n:
    :param d:
    :param banks:
    :return:
    """
    banks = sorted(banks, key=lambda x: x[1], reverse=True)
    print(banks)
    money = banks[0][1]
    j = 1
    while abs(banks[0][0] - banks[j][0]) < d:
        j += 1
    print(money + banks[j][1])



# n,d = [int(x) for x in input().split()]
# banks = []
# for i in range(n):
#     banks.append([int(x) for x in input().split()])
# solve(n,d,banks)

n, d = 6, 2
banks = [[1, 1], [7, 5], [6, 6], [5, 5], [10, 2], [11, 2], [9, 1]]
solve(n, d, banks)
solve2(n, d, banks)
solve4(n, d, banks)
