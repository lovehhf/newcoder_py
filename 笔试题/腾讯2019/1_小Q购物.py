# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小Q去商场购物，经常会遇到找零的问题。
小Q现在手上有n种不同面值的硬币，每种面值的硬币都有无限多个。
为了方便购物，小Q希望带尽量少的硬币，并且要能组合出1到m之间（包含1和m）的所有面值。

输入格式
第一行包含两个整数m和n。

接下来n行，每行一个整数，第 i+1 行的整数表示第 i 种硬币的面值。

输出格式
输出一个整数，表示最少需要携带的硬币数量。

如果无解，则输出-1。

数据范围
1≤n≤10^0,
1≤m≤10^9，
1≤硬币面值≤10^9
输入样例：
20 4
1
2
5
10
输出样例：
5
"""

class Solution(object):
    def min_coin_num(self,coins,m,n):
        coins.sort()
        if coins[0]!=1:
            return -1
        # 删除值大于m的数
        while n>0 and coins[n-1]>m:
            coins.pop()
            n -= 1
        coins.append(m + 1)
        res = 0
        s = 0
        for i in range(n):
            import math
            k = math.ceil((coins[i + 1] - 1 - s) / coins[i])
            print(k)
            res += k
            s += k * coins[i]
        return res

s = Solution()
m,n = [int(x) for x in input().split(' ')]
coins = []
for _ in range(n):
    coins.append(int(input()))
# m,n = 20,4
# coins = [1,2,5,10]
print(s.min_coin_num(coins,m,n))
