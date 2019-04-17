# -*- coding:utf-8 -*-

__author__ = 'huanghf'


class Solution:
    def jumpFloorII(self, number):
        if number==1:
            return 1
        if number==2:
            return 2
        l = [1,2]
        for i in range(2,number):
            l.append(sum(l)+1)

        return l[-1]

s = Solution()
print(s.jumpFloorII(3))