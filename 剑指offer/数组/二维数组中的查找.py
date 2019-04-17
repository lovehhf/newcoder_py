# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
]
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m, n = len(array), len(array[0])
        if m == 0 or n == 0:
            return False
        # L, R = 0, m-1
        if target<array[0][0] or target>array[-1][-1]:
            return False

        # 找到在哪一行
        # while L <= R:
        #     mid = (L + R) // 2
        #     if array[mid][-1] == target:
        #         return True
        #     elif array[mid][-1] < target:
        #         L = mid + 1
        #     else:
        #         R = mid - 1

        for r in range(m):
            if array[r][0]<target and array[r][-1]>target:
                L, R = 0, n-1
                while L <= R:
                    mid = (L + R) // 2
                    if array[r][mid] == target:
                        return True
                    elif array[r][mid] < target:
                        L = mid + 1
                    else:
                        R = mid - 1
            if array[r][0]>target:
                return False
        return False


s = Solution()
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target = 7

print(s.Find(target, array))
