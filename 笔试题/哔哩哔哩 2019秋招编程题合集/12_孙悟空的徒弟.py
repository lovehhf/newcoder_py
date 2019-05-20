# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：3秒
空间限制：131072K

打败魔人布欧以后，孙悟空收了n个徒弟，每个徒弟战斗力各不相同。他教导所有的徒弟和体术，**合体后战斗力为原战斗力相乘。**
任何两个徒弟都可以合体，所以一共有n*(n-1)/2种合体徒弟。有一天，他想考验一下孙悟天战斗力如何，
希望在所有n*(n-1)/2种合体徒弟中选择战斗力第k高的，与孙悟天对战。可是孙悟空徒弟太多了，他已然懵逼，于是找到了你，请你帮他找到对的人。

输入描述:
第一行两个int。徒弟数量：n <= 1*10^6；战斗力排名:k <= n*(n-1)/2
第二行空格分隔n个int，表示每个徒弟的战斗力。

输出描述:
战斗力排名k的合体徒弟战斗力。

输入例子1:
5 2
1 3 4 5 9

输出例子1:
36


"""

def solve(n,k,nums):
    """
    暴力 65.00%
    :param n:
    :param k:
    :param nums:
    :return:
    """
    ls = []
    for i in range(n-1):
        for j in range(i+1,n):
            ls.append(nums[i]*nums[j])
    ls = sorted(ls,reverse=True)
    return ls[k-1]

n,k = list(map(int,input().split()))
nums = list(map(int,input().split()))
# n,k = 5,2
# nums = [1, 3, 4, 5, 9,7]
print(solve(n,k,nums))