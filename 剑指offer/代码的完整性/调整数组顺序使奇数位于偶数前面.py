# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""

class Solution:
    def reOrderArray(self, array):
        n = len(array)
        # 类似冒泡排序
        for i in range(n):
            for j in range(n-1,i,-1):
                if array[j]%2==1 and array[j-1]%2==0:
                    array[j], array[j - 1]  = array[j-1], array[j]

    def reOrderArray2(self, array):
        return [x for x in array if x%2!=0]+[x for x in array if x%2==0]

array = [2,2,3,4,5,6,7,8]
s = Solution()
print(s.reOrderArray(array))