# -*- coding:utf-8 -*-

__author__ = 'huanghf'


def fun(n, a):
    res = [1] * n
    if n == 1:
        res = [1]
        return res
    min_num = min(a)
    min_index = a.index((min_num))
    # print(min_index)
    for i in range(min_index + 1, min_index + n):
        # print(i)

        index = i % n
        last_index = (i - 1) % n
        next_index = (i + 1) % n
        # print(index,last_index,next_index)
        if i % n == 0:
            last_index = n - 1
        if a[index] > a[last_index] and a[index] > a[next_index]:
            res[index] = max(res[last_index], res[next_index]) + 1

        if a[index] > a[last_index] and a[index] <= a[next_index]:
            res[index] = res[last_index] + 1
        if a[index] <= a[last_index] and a[index] > a[next_index]:
            res[index] = res[next_index] + 1
            if a[index] < a[last_index]:
                res[last_index] += 1
        if a[index] <= a[last_index] and a[index] <= a[next_index]:
            res[index] = 1
        # print(res[index])

    print(res)
    # print(sum(res))
    # if n == 1:
    #     return 1
    # if n == 2:
    #     if a[n-1]>a[n-2]:
    #         return fun(n-1,a[:-1])+


fun(6, [3, 2, 3, 5, 1, 4])

fun(4, [1, 2, 3, 3])

# N = int(input())
# for i in range(N):
#     n = int(input())
#     a = list(map(int,input().split(' ')))
#     fun(n,a)
