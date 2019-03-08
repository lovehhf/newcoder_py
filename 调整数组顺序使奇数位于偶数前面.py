# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def reOrderArray(array):
    # write code here
    l = []
    r = []
    for i in range(len(array)):
        if array[i]%2==0:
            r.append(array[i])
        else:
            l.append(array[i])

    return l+r

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]

    print(reOrderArray(array))