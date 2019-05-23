# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
题目描述
统计一个数字在排序数组中出现的次数。


[1,3,5,7,9],3 -> mid = 5>3 ->r=mid [1,3,5] 3=3 r=mid [1,3],1<3 l=mid+1

[1,3,5,7,9],7 -> mid=5<7 l=mid [5,7,9] 7=mid->l=mid [7,9],9>mid r=mid-1

[1,1] mid=0,r=mid=0
[1,1] mid=1,l=mid=1
找左边界:if nums[mid]>=target R=mid else L=mid+1
找右边界:if nums[mid]<=target L=mid else R=mid-1
"""


class Solution:
    def get_left_border(self, nums, k):
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) >> 1
            if nums[mid] < k:
                L = mid + 1
            else:
                R = mid
        return L

    def get_right_border(self, nums, k):
        L, R = 0, len(nums) - 1
        while L < R:
            mid = (L + R + 1) >> 1
            if nums[mid] <= k:
                L = mid
            else:
                R = mid - 1
        return L

    def GetNumberOfK(self, data, k):
        """
        两次二分算出左右边界
        :param data:
        :param k:
        :return:
        """
        if not data or data[0]>k or data[-1]<k:
            return 0
        l = self.get_left_border(data, k)
        r = self.get_right_border(data, k)
        # print(l, r)
        return r - l + 1 if r>=l else 0


s = Solution()
nums = [1, 3, 3, 3, 3, 4, 5]
k = 3
print(s.GetNumberOfK(nums, k))
