# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        """
        方法一
        遍历一次 使用字典记录数字出现的次数
        :param array:
        :return:
        """
        from collections import defaultdict
        d = defaultdict(int)
        for num in array:
            d[num] = d.get(num,0) +1
        res = [k for k,v in d.items() if v==1]
        return res

    def FindNumsAppearOnce2(self, array):
        """
        位运算 忘了怎么写了
        :param array:
        :return:
        """
        pass

s = Solution()
print(s.FindNumsAppearOnce([1,2,3,3,4,4]))