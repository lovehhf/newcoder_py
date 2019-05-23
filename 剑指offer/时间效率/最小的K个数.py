# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
        使用heapq库,堆排
        时间复杂度O(nlogk)
        :param tinput:
        :param k:
        :return:
        """
        import heapq

        if k>len(tinput):
            return []
        return heapq.nsmallest(k,tinput)


nums = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers_Solution(nums,4))
