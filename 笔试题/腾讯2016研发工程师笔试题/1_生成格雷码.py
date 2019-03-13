# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同， 则称这种编码为格雷码(Gray Code)，请编写一个函数，使用递归的方法生成N位的格雷码。

给定一个整数n，请返回n位的格雷码，顺序为从0开始。

测试样例：
1
返回：["0","1"]

2 ["00","01","11","10"]

3 ['000','001','011,'010','110','111','101','100']

f(1) = ["0","1"]
f(2) = ["0" + "0","0" + "1"] + ["1"+"1","1"+"0"]
.....
f(n) = ['0'+x for x in f(n-1)] + ['1'+x for x in f(n-1)]
"""


class GrayCode:
    def getGray(self, n):
        # write code here
        if n == 1:
            return ["0","1"]
        return ['0'+x for x in self.getGray(n-1)] + ['1'+x for x in reversed(self.getGray(n-1))]

gc = GrayCode()

print(gc.getGray(6))