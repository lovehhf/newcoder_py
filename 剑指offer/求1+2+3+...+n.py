# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""


class Solution:
    def Sum_Solution(self, n):
        # write code here
        #
        ans=n
        # 逻辑and与有个短路特点，前面为假，后面不计算。 ans = 0时 跳出递归
        # a  and  b，a为False，返回a，a为True，就返回b
        temp=ans and self.Sum_Solution(n-1)
        # print(temp)
        ans=ans+temp
        return ans

s = Solution()
n = 10
print(s.Sum_Solution(10))