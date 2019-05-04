# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
我们称一个矩阵为黑白矩阵，当且仅当对于该矩阵中每一个位置如(i, j)，其上下左右四个方向的数字相等，
即(i-1, j)、(i+1, j)、(i, j-1)、(i, j+1)四个位置上的数字两两相等且均不等于(i, j)位置上的数字。（超出边界的格子忽略）

现在给出一个 n*m 的矩阵，我们想通过修改其中的某些数字，使得该矩阵变成黑白矩阵，请问最少需要修改多少个数字。

输入格式
第一行包含两个整数n和m，表示矩阵的长宽。

接下来n行，每行包含m个整数，用来表示整个矩阵。

输出格式
仅包含一个整数，表示原矩阵变为黑白矩阵最少修改的数字数量。

数据范围
1≤n,m≤10^5,
1≤n∗m≤10^5
输入样例1：
3 3
1 1 1
1 1 1
1 1 1
输出样例1：
4
输入样例2：
3 3
1 1 1
1 5 1
1 1 1
输出样例2：
4

10 10
1 1 2 2 2 1 2 2 2 1
2 1 2 1 1 2 1 1 1 2
2 2 2 1 2 2 1 1 1 2
2 1 1 1 1 1 1 1 1 2
1 2 2 2 2 2 1 1 1 1
1 2 2 2 2 1 2 1 2 1
2 2 2 2 1 1 2 1 2 2
2 2 1 1 2 1 1 2 2 1
2 2 2 1 2 2 2 1 1 2
1 1 2 1 1 1 1 2 1 2
49

https://www.nowcoder.com/discuss/182876
大致思路：修改后的矩阵要像一个国际象棋的棋盘一样，黑格数字全部一样，白格数字全部一样。
分别统计所有白格、黑格中出现次数最多的数字和第二多的数字。
- 如果黑白格中出现最多次数的数字不相等，直接输出n*m - 黑格出现次数最多的数字的次数 - 白格出现次数最多的数字的次数。
- 如果黑白格中出现最多次数的数字相等，那么输出n*m - 黑格出现次数最多的数字的次数 - 白格出现次数第二多的数字的次数 和 n*m - 白格出现次数最多的数字的次数 - 黑格出现次数第二多的数字的次数 的最小值。

分两组统计（i+j%2）数字出现次数，每组保留前二多的，因为两组不能同时取同一个数，根据情况选取，最后用总数减去即可，ac。

链接：https://www.nowcoder.com/discuss/183193
把矩阵看作像国际象棋棋盘一样的黑白矩阵。最终的目的就是要黑格子中的数字相同，白格子中的数字相同。同时我们希望用最少的修改次数使矩阵变成这种状态。
分别统计黑格子和白格子中出现最多的数字和第二多的数字以及出现的次数。
如果黑格子中出现最多的数字和白格子中出现最多的数字不一样，那么只需要分别把黑白格子中除了出现最多的数字以外的其他数字改为和出现最多的数字相同。就可以达到满足题意的状态，而且这种方法修改的次数是最少的。
再具体一点就是使用矩阵的大小减去黑白格子中出现最多的数字的个数，也就是减去不需要修改的数，剩下的就是需要修改的数字的个数。
如果黑格子中出现最多的数字和白格子中出现最多的数字一样。那么就要考虑出现第二多的数字了。那么这个时候可能有两种组合，
组合1：黑格子中出现最多的数字的个数和白格子中出现第二多的数字的个数相加
组合2：白格子中出现最多的数字的个数和黑格子中出现第二多的数字的个数相加
这个组合的数就是不需要修改的数的个数，哪个组合的数更大，就说明这个组合需要修改的数更少。所以用矩阵的大小减去更大的组合数，就是最少需要修改的次数。
"""


def main(n, m, grid):
    if m == 1 and n == 1:
        return 1
    d1 = {}
    d2 = {}
    res = 0
    for i in range(n):
        for j in range(m):
            key = grid[i][j]
            if (i + j) % 2:
                d1[key] = d1.get(key, 0) + 1
            else:
                d2[key] = d2.get(key, 0) + 1

    # 字典排序
    l1 = sorted(d1.items(), key=lambda x: x[1], reverse=True)
    l2 = sorted(d2.items(), key=lambda x: x[1], reverse=True)

    if l1[0][0] != l2[0][0]:
        res = m * n - (l1[0][1] + l2[0][1])
    else:
        l1.append((0, 0))
        l2.append((0, 0))
        if len(l1) > 1 and len(l2) > 1:
            res = m * n - max(l1[0][1] + l2[1][1], l2[0][1] + l1[1][1])
        # elif len(l1)==1 and len(l1)==1:
        #     res = m*n - max(l1[0][0],l2[0][0])
        # elif len(l1)==1:
        #     res = m * n - max(l1[0][1] + l2[1][1], l2[0][1])
        # elif len(l2)==1:
        #     res = m * n - max(l2[1][1], l2[0][1] + l1[1][1])
    return res


n, m = list(map(int, input().split(' ')))
grid = []
for i in range(n):
    grid.append(list(map(int, input().split(' '))))
res = main(n, m, grid)
print(res)
