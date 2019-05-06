# -*- coding:utf-8 -*-

__author__ = 'huanghf'

from collections import Counter

def MoreThanHalfNum_Solution(numbers):
    # write code here
    c = Counter(numbers)
    max_c = c.most_common(1)[0]
    if max_c[1]>len(numbers)//2:
        return max_c[0]
    # for i in set(numbers):
    #     if numbers.count(i) > len(numbers) // 2:
    #         return i
    return 0

print(MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))