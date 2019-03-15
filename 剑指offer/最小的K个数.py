# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def GetLeastNumbers_Solution(tinput, k):
    """
    选择排序
    :param tinput:
    :param k:
    :return:
    """
    # write code here
    n = len(tinput)
    if k > n:
        return []
    for i in range(k):
        min_index = i
        for j in range(i,n-1):
            if tinput[j+1] < tinput[min_index]:
                min_index = j+1
        swap(tinput,min_index,i)
    return tinput[:k]

tinput = [4,5,1,6,2,7,3,8]
k = 4
print(GetLeastNumbers_Solution(tinput, k))