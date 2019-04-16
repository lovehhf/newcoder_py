# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


class Solution:
    def PrintMinNumber2(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        from functools import cmp_to_key
        array = sorted(numbers,key=cmp_to_key(lmb))
        return ''.join([str(i) for i in array])

    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        numbers = list(map(str, numbers))
        n = len(numbers)
        # 冒泡排序
        for i in range(n - 1):
            for j in range(0, n-i-1):
                # j+1和j拼装出的数<j和j+1拼装出的数时 交换j和j+1 保证更小的在前面
                if int(numbers[j+1] + numbers[j]) < int(numbers[j] + numbers[j+1]):
                    numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
                # print(numbers)
        return ''.join(numbers)

s = Solution()
print(s.PrintMinNumber2([3, 32, 321]))
