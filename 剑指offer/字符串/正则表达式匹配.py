# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


class Solution:
    def match(self, s, p):
        """
        # s, pattern都是字符串
        dp[i][j]: s的前i个字符与p的第j个字符是否匹配
        :param s:
        :param p:
        :return:
        """
        s = ' ' + s
        p = ' ' + p
        m, n = len(s), len(p)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(1, n):
                if i > 0 and (s[i] == p[j] or p[j] == '.'):
                    dp[i][j] = dp[i - 1][j - 1]
                if p[j] == '*':
                    dp[i][j] = dp[i][j - 2] | dp[i][j]
                    if i > 0 and (p[j - 1] == '.' or s[i] == p[j - 1]):
                        dp[i][j] = dp[i][j] | dp[i - 1][j] | dp[i - 1][j - 2]
        # for i in dp:
        #     print(i)
        return dp[-1][-1]


s = ""
p = "."
sol = Solution()
print(sol.match(s, p))
