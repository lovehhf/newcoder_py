# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

[2,3,1,0,2,5,3]
1,[1,3,2,0,2,5,3]
2,[3,1,2,0,2,5,3]
3,[0,1,2,3,2,5,3]
4,[0,1,2,3,2->2与他的位置上的数重复了,返回
if i==t:i++
else:if nums[i]!=nums[t],交换两个元素,t回到属于他的位置,否则说明有重复元素。
时间复杂度O(n) 空间复杂度O(1)
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        i = 0
        while i < n:
            t = numbers[i]
            if i == t:
                i += 1
            else:
                if numbers[i] != numbers[t]:
                    numbers[i], numbers[t] = numbers[t], numbers[i]
                else:
                    duplication[0] = numbers[i]
                    return True
        return False


s = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
duplication = [0]
s.duplicate(nums, duplication)
print(duplication)
