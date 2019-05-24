# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
小易有一个长度为n的整数序列,a_1,...,a_n。然后考虑在一个空序列b上进行n次以下操作:
1、将a_i放入b序列的末尾
2、逆置b序列
小易需要你计算输出操作n次之后的b序列。
输入描述:
输入包括两行,第一行包括一个整数n(2 ≤ n ≤ 2*10^5),即序列的长度。
第二行包括n个整数a_i(1 ≤ a_i ≤ 10^9),即序列a中的每个整数,以空格分割。
输出描述:
在一行中输出操作n次之后的b序列,以空格分割,行末无空格。
示例1
输入
4
1 2 3 4
输出
4 2 1 3

这里题目理解错了,b初始是空的,这样样例只是凑巧对了
2 3 4 1 -> 1 4 3 2
[1, 3, 2, 4]->[4, 2, 3, 1]
[4, 2, 1, 3]->[3, 1, 2, 4]
[3, 1, 2, 4]->[4, 2, 1, 3]
似乎没啥规律 直接暴力

1 2 3
1
1 2->2 1
2 1 3 -> 3 1 2

找规律
[0] -> [0]
[0, 1] -> [1, 0]
[0, 1, 2] -> [2, 0, 1]
[0, 1, 2, 3] -> [3, 1, 0, 2]
[0, 1, 2, 3, 4] -> [4, 2, 0, 1, 3]
[0, 1, 2, 3, 4, 5] -> [5, 3, 1, 0, 2, 4]
[0, 1, 2, 3, 4, 5, 6] -> [6, 4, 2, 0, 1, 3, 5]
[0, 1, 2, 3, 4, 5, 6, 7] -> [7, 5, 3, 1, 0, 2, 4, 6]
[0, 1, 2, 3, 4, 5, 6, 7, 8] -> [8, 6, 4, 2, 0, 1, 3, 5, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] -> [9, 7, 5, 3, 1, 0, 2, 4, 6, 8]
"""


def solve2(n, A):
    """
    找规律
    偶数: [9, 7, 5, 3, 1, 0, 2, 4, 6, 8] n-1,n-3...1,0,2,4,6,..n-2
    奇数: [8, 6, 4, 2, 0, 1, 3, 5, 7]   n-1,n-3...2,0,1,3,5,..n-2
    :param n:
    :param A:
    :return:
    """
    res = []
    if n%2: # 奇数
        res += [A[i] for i in range(n - 1, -1, -2)]
        res += [A[i] for i in range(1, n, 2)]
    else: # 偶数
        res += [A[i] for i in range(n - 1, 0, -2)]
        res += [A[i] for i in range(0, n, 2)]
    return res

def solve(n, A):
    """
    暴力, 超时
    :param n:
    :param A:
    :return:
    """
    B = []
    for i in range(n):
        B.append(A[i])
        B = B[::-1]
    # print(A, '->', B)
    return B


# def solve(n, nums):
#     for i in range(n):
#         nums = list(reversed(nums[:i] + nums[i + 1:] + [nums[i]]))
#         print(nums)
#     return nums


def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(' '.join([str(x) for x in solve(n, nums)]))


def test():
    n = 9
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 10):
        print(solve(i + 1, list(range(0, i + 1))))
        print(solve2(i + 1, list(range(0, i + 1))))

test()
