# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）

输入描述:
输入包括一个整数n,(3 ≤ n < 1000)

输出描述:
输出对数

输入例子1:
10

输出例子1:
2
"""
def get_all_prime_num(n):
    l = [2]
    if n == 2:
        return [2]
    for i in range(3,n):
        tmp = 0
        for j in l:
            if i%j == 0:
                tmp = 1
                break
        if tmp!=1:
            l.append(i)
    return l

def count_pair_num(n):
    l = get_all_prime_num(n)
    count = 0
    for i in l:
        for j in l:
            if i+j == n and i<=j:
                count += 1
    return count

# print(count_pair_num(3))
n = int(input())
print(count_pair_num(n))
