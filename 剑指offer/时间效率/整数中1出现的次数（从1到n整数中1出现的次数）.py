# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

找规律:
112
13+13+12

2121
1000+(2*100+22)+22*10+213

53116
10000+6*1000+53*100+17+531*10+7+5312
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        s = str(n)
        m = len(s)
        res = 0
        tmp = 1
        for i in range(m - 1, 0, -1):
            if s[i] == '0':
                res += int(s[:i]) * tmp
            elif s[i] == '1':
                res += int(s[:i]) * tmp + int(s[i + 1:]) + 1
            else:
                res += int(s[:i]) * tmp + tmp
            tmp *= 10
        if s[0] > '1':
            res += tmp
        if s[0] == '1':
            if m > 1:
                res += int(s[1:]) + 1
            else:
                return 1
        return res


    def NumberOf1Between1AndN_Solution2(self, n):
        """
        暴力
        :param n:
        :return:
        """
        return ''.join([str(x) for x in range(1, n + 1)]).count('1')


s = Solution()
n = 21345
print(s.NumberOf1Between1AndN_Solution(n))
print(s.NumberOf1Between1AndN_Solution2(n))
