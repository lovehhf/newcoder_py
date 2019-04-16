# -*- coding:utf-8 -*-

__author__ = 'huanghf'

# N = int(input())
# M = list(map(int,input().split(' ')))

N = 3
M = [1, 6, 4]

L = min(M)
R = max(M)

def fun(E):
    for i in range(N):
        if E<M[i]:
            E -= M[i] - E
        else:
            E += E - M[i]
        if E<0:
            return False
    return True

while L<R:
    mid = (L+R)//2

    # 模拟
    if not fun(mid):
        L = mid + 1
    else:
        R = mid
    print(L,R)

print(L)