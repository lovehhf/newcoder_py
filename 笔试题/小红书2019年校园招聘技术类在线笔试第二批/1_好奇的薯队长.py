# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
薯队长在平时工作中需要经常跟数字打交道，某一天薯队长收到了一个满是数字的表格，薯队长注意到这些数字里边很多数字都包含1，比如101里边包含两个1，616里包含一个1。
请你设计一个程序帮薯队长计算任意一个正整数n(0<n<=2147483647)，从1到n（包括n）的所有整数数字里含有多少个1。

输入描述:
正整数n(0<n<=2147483647)

输出描述:
从1到n（包括n）的所有整数数字里含有多少个1

输入例子1:
1

输出例子1:
1

输入例子2:
13

输出例子2:
6

例子说明2:
从1到13（包括13）有13个数字，其中包含1的数字有1，10，11，12，13，
这些数字里分别有1，1，2，1，1个1，所以从1到13（包括13）的整数数字中一共有1+1+2+1+1=6个1


888->800+80+8->260+18+1

1~100->10+10+1=21个 个位1:10个+十位1:10个+百位1:1个

500->百位1:100个 个位1:500//10=50个 十位1:5*10个(01*,11*,21*,31*,41*) = 100+50+50=200个

4649816->1*1000000+5*100000+47*10000+465*1000+4650*100+46498*10-3+464982
"""


def solve2(n):
    """
    暴力  内存超过限制 case通过率为60.00%
    :param n:
    :return:
    """
    c = 0
    # for i in range(n+1):
    #     if '1' in str(i):
    #         c+=str(i).count('1')
    #         print(i,c)
    s = ''.join(map(str, range(n + 1)))
    print(s.count('1'))


def solve(n):
    count = 0
    i = 1
    while i <= n:
        d = i * 10
        k = n // d * i + min(max(n % d - i + 1, 0), i)
        count +=k
        # print(k)
        i *= 10
    print(count)

n = 4649816
solve(n)
solve2(n)
