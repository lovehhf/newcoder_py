# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


class Solution:
    # s字符串
    def isNumeric(self, s):
        if not s:
            return False
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        n = len(s)
        dot = 0
        count_e = 0
        for i in range(n):
            if '0' <= s[i] <= '9':
                continue
            elif s[i] == '.' and dot < 1 and count_e < 1:
                dot += 1
            elif i > 0 and i < n - 1 and (s[i] == 'e' or s[i] == 'E'):
                count_e += 1
            elif i > 0 and i < n - 1 and (s[i] == '-' or s[i] == '+'):
                if s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            else:
                return False
        return n > 0


s = "123.45e+6"
sol = Solution()
print(sol.isNumeric(s))
