# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 
如果没有则返回 -1（需要区分大小写）.
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
        先遍历一遍s将字符出现的次数存在字典里面
        再遍历一遍s,如果遍历到的字符只出现一次 返回这个字符的位置
​       时间复杂度0(n) 空间复杂度O(n)
        :param s:
        :return:
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0) +1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1

    def FirstNotRepeatingChar2(self, s):
        """
        使用filter
        代码复杂度-- 时间复杂度++
        :param s:
        :return:
        """
        res = list(filter(lambda x:s.count(x)==1,s))
        return s.index(res[0]) if res else -1


s = "google"
sol = Solution()
print(sol.FirstNotRepeatingChar2(s))
