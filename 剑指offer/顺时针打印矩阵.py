# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

用旋转魔法的方式，一直取出第一行；
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，变为
4 5 6
7 8 9
再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。
"""

def printMatrix(matrix):

    # res = []
    # n = len(matrix)    # 行数
    # m = len(matrix[0]) # 列数
    # if n == 1 and m == 1:
    #     res = [matrix[0][0]]
    #     return res
    # circle = (min(m, n) + 1) // 2  # 圈数
    # for o in range(circle):
    #     [res.append(matrix[o][i]) for i in range(o, m - o)]
    #     [res.append(matrix[j][m - 1 - o]) for j in range(o, n - o) if matrix[j][m - 1 - o] not in res]
    #     [res.append(matrix[n - 1 - o][k]) for k in range(m - 1 - o, o - 1, -1) if matrix[n - 1 - o][k] not in res]
    #     [res.append(matrix[l][o]) for l in range(n - 1 - o, o - 1, -1) if matrix[l][o] not in res]
    # return res


    # result = []
    # while matrix:
    #     result += matrix.pop(0)
    #     if matrix:
    #         matrix = [[row[col] for row in matrix] for col in reversed(range(len(matrix[0])))]    # 逆时针旋转
    # return result

    # write code here
    result = []
    while matrix:
        result += matrix.pop(0)
        # print(matrix)
        if matrix:
            m = len(matrix)  # 行数
            n = len(matrix[0])  # 列数
            l1 = []
            l2 = []
            for i in list(reversed(range(0, n))):
                for j in range(0, m):
                    l1.append(matrix[j][i])
                    # print(l1)
                l2.append(l1)
                l1 = []
                # print(m,n,l2)
            matrix = l2
    return result

a = [[1,2,3],[4,5,6],[7,8,9]]
print(printMatrix(a))