# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def jumpFloorII(number):
    from functools import reduce
    # write code here
    if number==1:
        return 1
    if number==2:
        return 2
    l = [1,2]
    for i in range(2,number):
        l.append(sum(l)+1)

    return l[-1]

print(jumpFloorII(3))