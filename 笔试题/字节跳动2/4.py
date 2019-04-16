# -*- coding:utf-8 -*-

__author__ = 'huanghf'



from  itertools import permutations

n = int(input())
N = []
for i in range(n):
    line = list(map(int,input().split(' ')))
    N.append(line)

# n = 4
# N = [[0, 2, 6, 5],
#      [2, 0, 4, 4],
#      [6, 4, 0, 2],
#      [5, 4, 2, 0]]

# dp[i][j]表示从i到j最低花销
# dp = [[0]*n]*n
t = []

for i in permutations(list(range(1,n))):
    t.append(list(i))

t = [[0]+x+[0] for x in t]

def fun(x):
    tmp = []
    for i in range(1,n+1):
        tmp.append([x[i-1],x[i]])
    return tmp

# 所有路线
t = list(map(fun,t))

t1 = [sum(list(map(lambda a:N[a[0]][a[1]],x))) for x in t]

# 最少花费
print(min(t1))