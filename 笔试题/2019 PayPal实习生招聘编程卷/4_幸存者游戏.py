# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
有n个同学围成一圈，其id依次为1，2，3...n（n号挨着1号）。
现在从1号开始报数，第一回合报到m的人就出局，第二回合从出局的下一个开始报数，报到m^2的同学出局。
以此类推直到最后一个回合报到m^(n-1)的人出局，直到剩下最后一个同学。输出这个同学的编号。n<=15,m<=5


输入描述:
每一行第一个数字代表n，第二个数字代表m

输出描述:
输出最后剩下同学的编号

输入例子1:
5 2

输出例子1:
5

1 2 3 4 5 -> 2, 1开始，删掉2
1 3 4 5 -> 4, 3开始，删掉1
3 4 5 ->8, 3开始,删掉4 
3 5 ->16, 5开始, 删掉3 剩下5


"""


def pop_num(nums, start_index, m):
    """
    从指定位置开始删除序号为m的数
    :param nums:
    :param start_index:
    :param m:
    :return:
    """
    # print(nums,start_index,m)
    pop_index = (start_index + m - 1) % len(nums)
    num = nums.pop(pop_index)
    # print(num)
    return nums, pop_index


def solve(n, m):
    nums = list(range(1, n + 1))
    cur = 0
    i = 0
    mm = m
    while len(nums) > 1:
        nums, i = pop_num(nums, i, mm)
        mm *= m
    return nums[0]

def test():
    n, m = 5, 2
    ans = solve(n, m)
    print(ans)

def main():
    n,m = list(map(int,input().split()))
    ans = solve(n,m)
    print(ans)

test()
