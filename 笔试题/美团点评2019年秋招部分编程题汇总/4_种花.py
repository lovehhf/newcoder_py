# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
公园里有N个花园，初始时每个花园里都没有种花，园丁将花园从1到N编号并计划在编号为i的花园里恰好种A_i朵花，
他**每天会选择一个区间[L，R]（1≤L≤R≤N）并在编号为L到R的花园里各种一朵花**，那么园丁至少要花多少天才能完成计划？

输入描述:
第一行包含一个整数N，1≤N≤10^5。

第二行包含N个空格隔开的整数A_1到A_N，0≤A_i≤10^4。

输出描述:
输出完成计划所需的最少天数。

输入例子1:
5
4 1 8 2 5

1->3 0 7 1 4 
2->3 0 6 0 3 -> 2+3+6+3=14
输出例子1:
14

单调栈
1. [4]
2. [4,1] -> [1]  3
3. [1,8]
4. [1,8] -> [1,2] 6
5. [1,2,5] 
"""

def solve(n,nums):
    """
    单调栈
    栈内只存储递增元素
    时间复杂度O(n)
    :param n:
    :param nums:
    :return:
    """
    nums.append(0)
    stack = []
    res = 0
    for i in range(n+1):
        if not stack or stack[-1]<=nums[i]:
            stack.append(nums[i])
        else:
            res += stack[-1]-nums[i]
            while stack and stack[-1]>nums[i]:
                stack.pop()
            stack.append(nums[i])
    print(res)

#
# n = 5
# nums = [3,5,4,8,2]

n = int(input())
nums = [int(x) for x in input().split()]
solve(n,nums)