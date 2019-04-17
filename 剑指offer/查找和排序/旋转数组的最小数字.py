# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个  非减排序的数组  的一个旋转，输出  旋转数组  的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        L = 0
        R = len(rotateArray)-1
        while L<R:
            mid = L+(R-L)//2
            # 右边有序的情况
            if rotateArray[mid]<rotateArray[R]:
                # 左边无序
                if rotateArray[mid]<rotateArray[L]:
                    R = mid
                # 左边有序
                else:
                    return rotateArray[L]
            # 左边有序的情况
            else:
                L = mid + 1
        return rotateArray[L]



rotateArray = [4,5,1,2,3]
s = Solution()
print(s.minNumberInRotateArray(rotateArray))