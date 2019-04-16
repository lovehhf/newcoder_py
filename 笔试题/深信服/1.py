# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def fun(L1):
    print(L1)
    if len(L1) == 1:
        return L1[-1]
    ret_list = []
    result = fun(L1[:-1])
    print(result)

    for r in result:
        for j in L1[-1]:
            ret_list.append(str(r)+'+'+str(j))
        print(ret_list)
    return ret_list

K,N = 3,4
L = [1,2,3]

# for i in range(K):
#     L.append(input())

# L = [i for i in range(len(L))]
# L1 = []
# for i in L:
#     L1.append(list(range(i+1)))
L1 = [[y for y in range(x+1)] for x in L]

print(L1)
print(fun(L1))
all_res = fun(L1)
ans = list(filter(lambda x:eval(x)==N,all_res))
print(list(map(lambda x:x.replace('+',''),ans)))
# for i in range(len(L1)):
#     for j in range()
