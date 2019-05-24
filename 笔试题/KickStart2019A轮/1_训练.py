# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
作为一名学校足球教练，你的任务是挑选一支由P个学生组成的团队代表你的学校。

共有N名学生供你挑选，第 i 名学生的技术等级为Si，这是一个正整数，表示他们的技术水平。

在你看来一个合理的团队中的P个球员的技术应该是相当的，这样才能使每个人都融入到队内。

在最开始，你可能无法直接选出一个配置合理的队伍，因此你将为一些学生提供一对一的辅导。

将一名学生的技术等级提高1需要你花费1个小时的时间来进行辅导。

比赛季很快就开始了（事实上，第一场比赛已经开始了！），所以你想知道训练出一个合理的团队，你需要提供的最少训练小时数是多少。

输入格式
第一行包含整数T，表示共有T组测试数据。

每组测试数据的第一行包含两个整数N和P。

第二行包含N个整数Si，其中第 i 个整数为第 i 个学生的技术等级。

输出格式
每组数据输出一个结果，每个结果占一行。

结果表示为“Case #x: y”，其中x为组别编号（从1开始），y为所需的最少训练小时数。

数据范围
1≤T≤100,
1≤Si≤10000,
2≤P≤N,
2≤N≤105
输入样例：
3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7
输出样例：
Case #1: 14
Case #2: 0
Case #3: 6
样例解释
在样例＃1中，你可以花费总共6个小时训练第一个学生，8个小时训练第二个学生，使得前三个学生的技能水平同为9。这是你可以花费的最短时间，因此答案是14。

在样例＃2中，你可以选择直接选择前两个学生而无需进行任何指导，因此答案为0。

在样例＃3中，P = N，因此每个学生都将加入您的团队。 你必须花6个小时训练第三个学生，这样所有人的技术等级都为7。 这是你可以花费的最短时间，所以答案是6。
"""


def solve(n, p, nums):
    """
    1. 预排序
    2. 找出p个相邻的数,最大的数*p - 这p个数的和就是训练这p个小朋友需要所花的时间
    3. 遍历找出最小的时间
    :param S:小朋友的水平
    :param N:总共N个小朋友
    :param P:选出P个小朋友
    :return:
    """
    nums.sort()
    pre_sum = [0] * (n + 1)  # 前缀和
    for i in range(1,n+1):
        pre_sum[i] = pre_sum[i - 1] + nums[i-1]
    res = float('inf')
    # print(pre_sum)
    for i in range(n - p + 1):
        res = min(res, nums[i + p - 1] * p - (pre_sum[i + p] - pre_sum[i]))
    return res
    # S.sort()
    # res = S[P - 1] * P - sum(S[:P])
    # for i in range(1, N - P + 1):
    #     tmp = S[i + P - 1] * P - sum(S[i:i + P])
    #     if tmp < res:
    #         res = tmp
    # return res


def main():
    t = int(input())
    for i in range(t):
        n, p = [int(x) for x in input().split()]
        nums = [int(x) for x in input().split()]
        ans = 'Case #%s: %s' % (i + 1, solve(n, p, nums))
        print(ans)


main()
