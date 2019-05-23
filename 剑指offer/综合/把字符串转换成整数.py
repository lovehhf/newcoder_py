# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
"""

class Solution:
    def StrToInt(self, s):
        """
        :param s:
        :return:
        """
        if not s:
            return 0
        res = 0
        sign = 1
        if s[0]=='-':
            sign = -1
            s = s[1:]
        elif s[0]=='+':
            s = s[1:]
        for i in s:
            if '0'<=i<='9':
                res = res*10 + ord(i)-ord('0')
            else:
                return 0
        return res*sign

s = "-"
sol = Solution()
print(sol.StrToInt(s))