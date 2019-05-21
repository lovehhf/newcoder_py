# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
Alice made some changes to a text file and she wants to know which lines are changed and compare the before and after line contents. 
Can you help her with this?

输入描述:
The first line contains two integers m (1<=m<=1000) and n (1<=n<=1000) – the number of lines in the original text and in the modified text separately. 
The following m lines are the original text and the next n lines compose the modified text. The length of each text line is in the range [0, 100]. 
Note that m may not be equal to n.

输出描述:
The result of the comparison is based on original text. 
If one line is not modified, just output the line with one leading space ‘ ‘.  
If this line is modified, output two lines: the original line leading with a ‘-‘ and the modified line leading with a ‘+’.

输入例子1:
3 4
a
bb
ccc
aa
bb
ccc
dddd

输出例子1:
-a
+aa
 bb
 ccc
+dddd

输入例子2:
3 3
a
b
c
xx
yy
c

输出例子2:
-a
-b
+xx
+yy
 c


['a', 'b', 'c'] ['xx', 'yy', 'c']
 
['a', 'b', 'c'] ['a', 'c', 'b']-> [a,-b,c,+b]
a
-b
c
+b
"""

#
# def solve(m, n, A, B):
#     res = []
#     i, j = 0, 0
#     while i < m and j < n:
#         if A[i] == B[j]:
#             res.append(' ' + A[i])
#             i += 1
#             j += 1
#         if i < m and j < n and A[i] != B[j]:
#             print(i,j,A[i],B[j])
#             res.append('-' + A[i])
#             i += 1
#     print(res)


def solve(m, n, A, B):
    """
    case通过率为50.00%  输出错误
    :param m:
    :param n:
    :param A:
    :param B:
    :return:
    """
    res = []
    i = 0
    x = min(m, n)
    # print(A,B)
    while i < x:
        j = i
        t1, t2 = [], []
        while j < x and A[j] != B[j]:
            t1.append('-' + A[j])
            t2.append('+' + B[j])
            j += 1
        res += t1 + t2
        i = j
        if i < x and A[i] == B[i]:
            res.append(' ' + A[i])
        i += 1
    if m < n:
        for i in range(m, n):
            res.append('+' + B[i])
    if m > n:
        for i in range(n, m):
            res.append('-' + A[i])
    # print(res)
    return res


def main():
    A, B = [], []
    m, n = [int(x) for x in input().split()]
    for _ in range(m):
        A.append(input())
    for _ in range(n):
        B.append(input())
    ans = solve(m, n, A, B)
    for i in ans:
        print(i)


def test():
    m, n = 3, 3
    A = ['a', 'b', 'c']
    B = ['a', 'c', 'b']
    print(solve(m, n, A, B))


test()
