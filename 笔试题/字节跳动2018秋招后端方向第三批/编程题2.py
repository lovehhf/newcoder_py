# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
https://blog.csdn.net/flushhip/article/details/78267949

有n个房间，现在i号房间里的人需要被重新分配，分配的规则是这样的：先让i号房间里的人全都出来，接下来按照 i+1, i+2, i+3, ... 的顺序依此往这些房间里放一个人，n号房间的的下一个房间是1号房间，直到所有的人都被重新分配。

现在告诉你分配完后每个房间的人数以及最后一个人被分配的房间号x，你需要求出分配前每个房间的人数。数据保证一定有解，若有多解输出任意一个解。


输入描述:
第一行两个整数n, x (2<=n<=10^5, 1<=x<=n)，代表房间房间数量以及最后一个人被分配的房间号；
第二行n个整数 a_i(0<=a_i<=10^9) ，代表每个房间分配后的人数。

输出描述:
输出n个整数，代表每个房间分配前的人数。

输入例子1:
3 1
6 5 1

输出例子1:
4 4 4

用例:
10 5
3 3 3 3 4 3 3 3 3 3

对应输出应该为:

0 0 0 31 0 0 0 0 0 0
"""

def check_ans(a,i,n,x):
    if (i+a[i])%n == x-1:
        return True
    else:
        return False



n,x = [int(x) for x in input().split(' ')]
a = list(map(int,input().split(' ')))

# n,x,a = 3, 1, [6, 5, 1]

# n,x = 5,4
# a = [3,1,3,1,3]  # 2 0 2 5 2

i = x-1
min_a = min(a)

# 如果有多个最小值 从后往前逆推找到第一个最小的值的index 这个就是i
for t in range(x-1,x-n-1,-1):
    if a[t] == min_a:
        if t < 0:
            i = n+t
        else:
            i = t
        break

# print(i)

ans = a
tmp = a[i]

for k,v in enumerate(a):
    if k != i:
        ans[k] -= tmp
    else:
        ans[i] = n*tmp
#
# print(ans)

for t in range(n):
    # print(ans)
    if check_ans(a,i,n,x):
        print(' '.join(list(map(str,ans))))
        break
    ans[i] += 1
    ans[(i+t)%n] -=1
