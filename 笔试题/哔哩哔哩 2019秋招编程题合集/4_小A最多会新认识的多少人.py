# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：1秒
空间限制：32768K

小A参加了一个n人的活动，每个人都有一个唯一编号i(i>=0 & i<n)，其中m对相互认识，在活动中两个人可以通过互相都认识的一个人介绍认识。
现在问活动结束后，小A最多会认识多少人？
输入描述:
第一行聚会的人数：n（n>=3 & n<10000）；
第二行小A的编号: ai（ai >= 0 & ai < n)；
第三互相认识的数目: m（m>=1 & m < n(n-1)/2）；
第4到m+3行为互相认识的对，以','分割的编号。

输出描述:
输出小A最多会新认识的多少人？

输入例子1:
7
5
6
1,0
3,1
4,1
5,3
6,1
6,5

输出例子1:
3
"""

def solve(m,n,a,A):
    """
    内存超限:您的程序使用了超过限制的内存 80%
    :param m:
    :param n:
    :param a:
    :param A:
    :return:
    """
    r = [set() for _ in range(n)] # 聚会的人的认识关系集合
    for x,y in A:
        r[x].add(y)
        r[y].add(x)
    res = 0
    vistied = r[a]
    queue = [x for x in vistied] # 小明认识的人进队列，bfs
    while queue:
        cur = queue.pop(0)
        for i in r[cur]:
            if not i in vistied and not i==a:
                vistied.add(i)
                queue.append(i)
                res += 1
    print(res)



n = int(input()) # 聚会的人数
a = int(input()) # 小A的编号
m = int(input()) # 互相认识的数目
A = []
for i in range(m):
    x,y = [int(x) for x in input().split(',')]
    A.append((x,y))

solve(m,n,a,A)