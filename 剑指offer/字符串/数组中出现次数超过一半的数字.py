# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

思路1:
  - 排序取中间值: 时间复杂度O(nlogn)
思路2:
  - 遍历一次,出现次数存在字典中 时间复杂度O(n) 空间复杂度O(n)
思路3：
  - 如果有符合条件的数字，则它出现的次数比其他所有数字出现的次数和还要多。
    在遍历数组时保存两个值：一是数组中一个数字，一是次数。
    遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；若次数为0，则保存下一个数字，并将次数置为1。
    遍历结束后，所保存的数字即为所求。然后再遍历一次判断它是否符合条件即可。
"""



class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        时间复杂度:O(n) 空间复杂度: 0(1)
        :param numbers:
        :return:
        """
        if not numbers:
            return 0
        res = numbers[0]
        times = 1
        n = len(numbers)
        for i in range(1,n):
            if times == 0:
                # 更新res的值为当前元素，并置次数为1
                res = numbers[i]
                times = 1
            elif(numbers[i] == res):
                times += 1
            else:
                times -= 1
        times = 0
        for i in range(n):
            if numbers[i] == res:
                times += 1
        return res if times>n//2 else 0

numbers = [1,2,3,2,4,2,5,2,3]
s = Solution()
print(s.MoreThanHalfNum_Solution(numbers))