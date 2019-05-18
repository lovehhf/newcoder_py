# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：1秒
空间限制：32768K

给定一个数字矩阵，请设计一个算法从左上角开始顺时针打印矩阵元素

输入描述:
输入第一行是两个数字，分别代表行数M和列数N；接下来是M行，每行N个数字，表示这个矩阵的所有元素；当读到M=-1，N=-1时，输入终止。

输出描述:
请按逗号分割顺时针打印矩阵元素（注意最后一个元素末尾不要有逗号！例如输出“1，2，3”，而不是“1，2，3，”），每个矩阵输出完成后记得换行

输入例子1:
3 3
1 2 3
4 5 6
7 8 9
-1 -1

输出例子1:
1,2,3,6,9,8,7,4,5

[4,5,6],
[7,8,9]
->[6,9],[5,8],[4,7]
"""
import sys

def rotate(matrix):
    """
    逆时针旋转矩阵
    :param matrix:
    :return:
    """
    return list(zip(*matrix))[::-1]

def print_matrix(matrix):
    """
    删除第一行,剩下的矩阵逆时针旋转
    :param m:
    :param n:
    :param matrix:
    :return:
    """
    res = []
    while matrix:
        cur = matrix.pop(0)
        res += [x for x in cur]
        matrix = rotate(matrix)
    print(','.join([str(x) for x in res]))

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print_matrix(matrix)

while True:
    matrix = []
    m, n = list(map(int, input().split()))
    if m==-1 and n==-1:
        break
    for i in range(m):
        matrix.append(list(map(int, input().split())))
    print_matrix(matrix)