# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

class Solution {
public:
    int Add(int num1, int num2)
    {
        int a,b,t;
        a = (num1&num2)<<1;
        b = num1^num2;
        while(a!=0){
            t = (a&b)<<1;
            b = a^b;
            a = t;
        }
        return b;
    }
};
"""


class Solution:
    def Add(self, num1, num2):
        """
        num1 ^ num2: 不带进位的加法
        (num1 & num2)<<1: 进位
        负数是噩梦，
        C++和Java就不用处理负数的问题Orz
        :param num1:
        :param num2:
        :return:
        """
        # while num1:
        #     num1, num2 = (num1 & num2) << 1, num1 ^ num2
        # return num2
        while num2:
            result = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = result
            num2 = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = ~(num1^0xffffffff)
        return result

num1 = -1
num2 = 2
s = Solution()
print(s.Add(num1, num2))
