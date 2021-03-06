# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
Z国的货币系统包含面值1元、4元、16元、64元共计四种硬币，以及面值1024元的纸币。

现在小Y使用1024元的纸币购买了一件价值为N的商品，请问最少他会收到多少硬币。

输入格式
共一行，包含整数N。

输出格式
共一行，包含一个数，表示最少收到的硬币数。

数据范围
0<N≤1024
输入样例：
200
输出样例：
17
样例解释
花200，需要找零824块，找12个64元硬币，3个16元硬币，2个4元硬币即可。
"""

# N=200
N = int(input())
def fun(n):
    count = 0
    a,b = divmod(n,64)
    count += a
    c,d  = divmod(b,16)
    count += c
    e,f  = divmod(d,4)
    count += e+f
    print(count)

fun(1024-N)