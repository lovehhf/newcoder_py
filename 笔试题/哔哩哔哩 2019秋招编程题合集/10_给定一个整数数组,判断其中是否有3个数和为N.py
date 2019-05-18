# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：1秒
空间限制：131072K

给定一个整数数组,判断其中是否有3个数和为N

输入描述:
输入为一行
逗号前为一个整数数组，每个元素间用空格隔开；逗号后为N

输出描述:
输出bool值
True表示存在3个和为N的数
False表示不存在3个和为N的数

输入例子1:
1 2 3 4 5,10

输出例子1:
True
"""


def three_sum(nums, target):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        k = target - nums[i]
        l, r = i + 1, n - 1
        while l < r:
            if nums[l] + nums[r] == k:
                return True
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
    return False

nums,target = input().split(',')
nums = [int(x) for x in nums.split()]
target = int(target)
res = three_sum(nums,target)
print(res)