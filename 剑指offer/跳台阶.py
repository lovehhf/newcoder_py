# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

链接：https://www.nowcoder.com/questionTerminal/8c82a5b80378478f9484d87d1c5f12a4
来源：牛客网

1.假设当有n个台阶时假设有f(n)种走法。
2.青蛙最后一步要么跨1个台阶要么跨2个台阶。
3.当最后一步跨1个台阶时即之前有n-1个台阶，根据1的假设即n-1个台阶有f(n-1)种走法。
4. 当最后一步跨2个台阶时即之前有n-2个台阶，根据1的假设即n-2个台阶有f(n-2 )种走法。
5.显然n个台阶的走法等于前两种情况的走法之和即f(n)=f(n-1)+f(n-2)。
6.找出递推公式后要找公式出口，即当n为1、2时的情况，显然n=1时f(1)等于1，f(2)等于2
"""

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        a,b = 1,2
        for i in range(0,number-1):
            a,b = b,a+b
        return a
