# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
在二维平面上有一个无限的网格图形，初始状态下，所有的格子都是空白的。

现在有n个操作，每个操作是选择一行或一列，并在这行或这列上选择两个端点网格，把以这两个网格为端点的区间内的所有网格染黑（包含这两个端点）。

问经过n次操作以后，共有多少个格子被染黑，重复染色同一格子只计数一次。

输入格式
第一行包含一个正整数n。

接下来n行，每行包含四个整数x1,y1,x2,y2，表示一个操作的两端格子坐标。
若x1=x2则是在一列上染色，若y1=y2则是在一行上染色。

保证每次操作是在一行或一列上染色。

输出格式
包含一个正整数，表示被染黑的格子的数量。

数据范围
1≤n≤10000,
−10^9≤x1,y1,x2,y2≤10^9
输入样例：
3
1 2 3 2
2 5 2 3
1 4 3 4
输出样例：
8
"""


class Solution(object):
    def __init__(self):
        self.res = 0

    def main(self, grid):
        ls1 = []
        ls2 = []
        for x1, y1, x2, y2 in grid:
            if y1 == y2:
                self.res += abs(x1 - x2) + 1
                ls1.append([(x1, x2), y1] if x1 < x2 else [(x2, x1), y1])
            if x1 == x2:
                self.res += abs(y1 - y2) + 1
                ls2.append([x1, (y1, y2)] if y1 < y2 else [x1, (y2, y1)])
            print(x1, y1, x2, y2,self.res)
        # print(ls1)
        # print(ls2)
        self.fun(ls1, ls2)
        # print(self.res)
        return self.res

    def fun(self, ls1, ls2):
        """
        求相交的格子数量
        :param ls1:
        :param ls2:
        :return:
        """
        ls1 = sorted(ls1, key=lambda x: x[1])
        ls2 = sorted(ls2, key=lambda x: x[0])
        m, n = len(ls1), len(ls2)
        print(ls1)
        print(ls2)
        i = 0
        while i < m - 1:
            if ls1[i][1] == ls1[i + 1][1]:
                print(ls1)
                if ls1[i][0][1] >= ls1[i + 1][0][0] and ls1[i + 1][0][1] >= ls1[i][0][0]:
                    a = min(ls1[i][0][1], ls1[i + 1][0][1]) - max(ls1[i][0][0], ls1[i + 1][0][0]) + 1
                    self.res -= a
                    t = [(min(ls1[i][0][0], ls1[i + 1][0][0]), max(ls1[i][0][1], ls1[i + 1][0][1])), ls1[i][1]]
                    print(t)
                    print(ls1[i], ls1[i + 1], a, "aaaaaaa")
                    ls1.pop(i + 1)
                    ls1.pop(i)
                    ls1.insert(i, t)
                    m -= 1
            else:
                i += 1
        i = 0
        while i < n - 1:
            if ls2[i][0] == ls2[i + 1][0]:
                if ls2[i][1][1] >= ls2[i + 1][1][0] and ls2[i + 1][1][1] >= ls2[i][1][0]:
                    a = min(ls2[i][1][1], ls2[i + 1][1][1]) - max(ls2[i][1][0], ls2[i + 1][1][0]) + 1
                    self.res -= a
                    t = [ls2[i][0], (min(ls2[i][1][0], ls2[i + 1][1][0]), max(ls2[i][1][1], ls2[i + 1][1][1]))]
                    print(t)
                    print(ls2[i], ls2[i + 1], a, "bbbbbb")
                    ls2.pop(i + 1)
                    ls2.pop(i)
                    ls2.insert(i, t)
                    n -= 1
            else:
                i += 1

        print(ls1)
        print(ls2)
        print(self.res)
        self.res = 0

        for r1, i in ls1:
            self.res += r1[1] - r1[0] + 1
            print(r1)
            print(self.res)
        for j, r2 in ls2:
            self.res += r2[1] - r2[0] + 1
            print(r2)
            print(self.res)

        for r1, i in ls1:
            for j, r2 in ls2:
                if r2[0]<=i<=r2[1] and r1[0]<=j<=r1[1]:
                    print(r1,j,r2,j)
                    self.res -= 1


# n = 3
# grid = [[1, 2, 3, 2], [2, 5, 2, 3], [1, 4, 3, 4]]
n = 10
grid = [[-1, 0, -1, 2], [-10, 6, -10, 3], [0, 4, 0, -3], [-4, 2, -4, 6], [-10, -6, -10, 6], [9, 5, 9, 7],
        [9, -1, 0, -1], [5, 2, 5, -7], [8, -1, -2, -1], [4, 7, 4, -7]]

# n = int(input())
# grid = []
# for i in range(n):
#     grid.append(list(map(int,input().split(' '))))
# print(grid)

s = Solution()
print(s.main(grid))
