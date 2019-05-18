# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
高贵的蕾米莉亚大小姐每天需要饮用定量 B 型血的红茶以保持威严，并且要分两杯在不同时段饮用。
女仆长十六夜咲夜每天可以制作很多杯不同剂量 B 型血的红茶供蕾米莉亚大小姐饮用。
某日，你和天才妖精琪露诺偷偷潜入红魔馆被咲夜抓住，要求在今日份的红茶中挑出所有满足大小姐要求的茶杯，否则……

输入描述:
每个样例有三行输入，第一行输入表示茶杯个数，第二行输入表示每份茶杯里的 B 型血剂量，第三行表示大小姐今天的定量

输出描述:
对每一个样例，输出所有可能的搭配方案，如果有多种方案，请按每个方案的第一杯 B 型血剂量的大小升序排列。
如果无法找到任何一种满足大小姐的方案，输出"NO"(不包括引号)并换行。

输入例子1:
7
2 4 6 1 3 5 7
7

输出例子1:
1 6
2 5
3 4
"""
def solve(n,k,nums):
    res = []
    d = {}
    for i in nums:
        d[i] = d.get(i,0) + 1
    for i in set(nums):
        if k-i in d:
            res.append(sorted([i,k-i]))
    res = list(set([tuple(x) for x in res]))
    res = sorted(res)
    if res:
        for x,y in res:
            print('%s %s'%(x,y))
    else:
        print("NO")

def solve2(n,k,nums):
    """
    超时
    :param n:
    :param k:
    :param nums:
    :return:
    """
    nums.sort()
    res = []
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j]==k:
                res.append([nums[i],nums[j]])
            if nums[i]+nums[j]>k:
                break
    if res:
        for x,y in res:
            print('%s %s'%(x,y))
    else:
        print("NO")

n = int(input())
nums = [int(x) for x in input().split()]
k = int(input())
solve(n,k,nums)