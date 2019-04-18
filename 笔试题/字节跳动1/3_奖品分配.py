# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
有n个人参加编程比赛，比赛结束后每个人都得到一个分数；现在所有人排成一圈（第一个和第n个相邻）领取奖品，要求：

1、如果某个人的分数比左右的人高，那么奖品数量也要比左右的人多；

2、每个人至少得到一个奖品；

问最少应该准备多少个奖品。

输入格式
第一行是整数T，表示测试样例个数。

每个测试样例的第一行是一个整数n，表示参加比赛的人数。

第二行是n个正整数a[i]，表示从第1个人到第n个人的分数。

输出格式
对每个测试样例，输出应该准备的最少奖品，每个结果占一行。

数据范围
1≤T≤10,
0<n<100000,
0<a[i]<100000
输入样例：
2
2
1 2
4
1 2 3 3
输出样例：
3
8
"""


def fun(n, nums):
    res = [1] * n
    if n == 1:
        res = [1]
        return res
    min_num = min(nums)
    min_index = nums.index((min_num))
    # print(min_index)
    for i in range(min_index + 1, min_index + n + 1):
        # print(i)

        index = i % n
        last_index = (i - 1) % n
        if nums[index] > nums[last_index]:
            res[index] = res[last_index] + 1
        while nums[index] < nums[last_index]:
            res[last_index] = max(res[last_index], res[index] + 1)
            index = (index - 1) % n
            last_index = (last_index - 1) % n
        return sum(res)


# N = int(input())
# for i in range(N):
#     n = int(input())
#     a = list(map(int,input().split(' ')))
#     print(fun(n,a))

print(fun(6, [3, 2, 3, 5, 1, 4]))
print(fun(4, [1, 2, 3, 3]))
