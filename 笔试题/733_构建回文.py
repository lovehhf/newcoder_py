# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
安娜有N个方块排成一排，每一方块都写着一个大写字母(A-Z中的一个)。

这些方块从左到右依次编号为1,2,…,N。

现在，她正在学习回文。

如果一个字符串不论是从左向右看，还是从右向左看，内容都一样，那么这个字符串就是一个回文字符串。

例如，ANNA,RACECAR,AAA和X都是回文字符串，而AB,FROG和YOYO则不是。

鲍勃想要测试一下安娜是否完全理解了回文这一概念，所以向她提出了Q个相关问题。

其中的第i个问题是：安娜能否使用从Li号到Ri号（包括端点方块）的所有方块，经过一系列排列使得它们构成一个回文结构？

如果可以，则回答“是”，如果不可以，则回答“否”。

在每个问题解答完毕之后，安娜都会把方块放回原来的位置。

请你帮助安娜求出，这些问题中有多少个问题可以回答“是”。

输入格式
第一行包含整数T，表示共有T组测试数据。

每组数据第一行包含两个整数N和Q，表示方块数量和问题数量。

第二行包含一个长度为N的由大写字母构成的字符串。

接下来Q行，每行包含两个整数Li和Ri，用来描述一个问题。

输出格式
每组数据输出一个结果，每个结果占一行。

结果表示为“Case #x: y”，其中x是组别编号（从1开始），y是可以回答“是”的问题数量。

数据范围
1≤T≤100,
1≤Li≤Ri≤N,
1≤N,Q≤105
输入样例：

2
7 5
ABAACCA
3 6
4 4
2 5
6 7
3 7
3 5
XYZ
1 3
1 3
1 3
1 3
1 3

输出样例：
Case #1: 3
Case #2: 0
样例解释
在样例＃1中，N = 7且Q = 5。

对于第一个问题，安娜需要使用方块AACC，经排列可得到回文结构ACCA（或CAAC）。
对于第二个问题，安娜需要使用方块A，这是回文结构。
对于第三个问题，安娜需要使用方块BAAC，这些方块无法排列得到回文结构。
对于第四个问题，安娜需要使用方块CA，这些方块无法排列得到回文结构。
对于第五个问题，安娜需要使用方块AACCA，经排列可得到回文结构ACACA（或CAAAC）。
总体来看，共有3个问题可以回答“是”，所以答案是3。

在样例＃2中，N = 3且Q = 5。

在这五个问题中，安娜都需要使用方块XYZ来创建回文，显然不可能，所以答案是0。
"""

# T = int(input())
# s = [[0 for _ in range(21)] for _ in range(26)]
# for C in range(1,T+1):
#     n,m = list(map(int, input().split(' ')))
#     S = input()
#     print(S)
#     for i in range(1,n+1):
#         for j in range(0,26):
#             s[j][i] = s[j][i-1] + int(S[i-1] == chr(j + ord('A')))
#     for i in s:
#         print(i)
#     res = 0
#     for i in range(m):
#         l,r = list(map(int, input().split(' ')))
#         cnt = 0
#         for j in range(26):
#             if (s[j][r] - s[j][l - 1]&l):
#                 cnt += 1
#         if cnt<=1:
#             res += 1
#     print('Case #%s: %s' % (C, res))

def fun2():
    from collections import defaultdict

    T = int(input())
    for x in range(1, T + 1):
        N, Q = map(int, input().split())
        characters = input()
        counters = [defaultdict(int)]
        for character in characters:
            counter = counters[-1].copy()
            counter[character] += 1
            counters.append(counter)
        y = 0
        for i in range(Q):
            L, R = map(int, input().split())
            odd_encountered = False
            for letter, R_count in counters[R].items():
                if (R_count - counters[L - 1][letter]) % 2:
                    if odd_encountered:
                        break
                    odd_encountered = True
            else:
                y += 1
        print("Case #{}: {}".format(x, y), flush = True)

# 方法一: 超时
def fun1():
    def check(s):
        l = [0] * 26
        # for i in range(26):
        #     l[i] = s.count(chr(i + ord('A')))
        for i in s:
            l[ord(i) - ord('A')] += 1
        # print(l)
        l = [x % 2 for x in l]
        if l.count(1) > 1:
            return False
        return True


    T = int(input())
    res = [0] * T
    for i in range(T):
        N, Q = list(map(int, input().split(' ')))
        S = input()
        for j in range(Q):
            L, R = list(map(int, input().split(' ')))
            if check(S[L - 1:R]):
                res[i] += 1

    for i in range(T):
        print('Case #%s: %s' % (i + 1, res[i]))

fun1()