# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
你打开了美了么外卖，选择了一家店，你手里有一张满X元减10元的券，店里总共有n种菜，第i种菜一份需要A_i元，
因为你不想吃太多份同一种菜，所以每种菜你最多只能点一份，现在问你最少需要选择多少元的商品才能使用这张券。

输入描述:
第一行两个正整数n和X，分别表示菜品数量和券的最低使用价格。（1≤n≤100, 1≤X≤10000） 接下来一行n个整数，第i个整数表示第i种菜品的价格。（1≤A_i≤100）

输出描述:
一个数，表示最少需要选择多少元的菜才能使用这张满X元减10元的券，保证有解。

输入例子1:
5 20
18 19 17 6 7

输出例子1:
23

贪心 6+17

dfs:
16.67%

01背包
"""


def dfs(nums, target, path, res):
    if target <= 0:
        res.append(path)
        return True
    for i in range(len(nums)):
        if i > 0 and path + nums[i - 1] > target:  # 未剪枝16.67% 剪枝后27.78%
            continue
        dfs(nums[i + 1:], target - nums[i], path + nums[i], res)


def main(n, x, nums):
    """
    :param n:
    :param x:
    :param nums:
    :return:
    """
    nums.sort()
    res = []
    dfs(nums, x, 0, res)
    print(res)
    print(min(res))


def solve(n, x, nums):
    """
    01背包
    dp[i][j]: 前i件物品是否能填满容量为j的背包
    每件物品可以选择拿与不拿
    状态转移方程:
    :param n:
    :param x:
    :param nums:
    :return:
    """
    dp = [[0] * (x + 1) for _ in range(n)]
    for i in range(1, x + 1):
        if i <= nums[0]:
            dp[0][i] = nums[0]
        else:
            dp[0][i] = 20000
    for i in range(1, n):
        for j in range(0, x + 1):
            if j <= nums[i]:
                dp[i][j] = min(nums[i], dp[i - 1][j])
            else:
                dp[i][j] = min(dp[i - 1][j], nums[i] + dp[i - 1][j - nums[i]])

    for i in dp:
        print(i)


# n,x = list(map(int,input().split()))
# nums = list(map(int,input().split()))
import random

# n, x = 5, 800
# nums = random.sample(list(range(1,100)),70)
n, x = 5, 20
nums = 5, 7, 16, 18, 19
print(nums)
solve(n, x, nums)
