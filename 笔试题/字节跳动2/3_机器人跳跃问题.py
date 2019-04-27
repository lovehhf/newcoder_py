# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
机器人正在玩一个古老的基于DOS的游戏。

游戏中有N+1座建筑——从0到N编号，从左到右排列。

编号为0的建筑高度为0个单位，编号为 i 的建筑高度为H(i)个单位。

起初，机器人在编号为0的建筑处。

每一步，它跳到下一个（右边）建筑。

假设机器人在第k个建筑，且它现在的能量值是E，下一步它将跳到第k+1个建筑。

如果H(k+1)>E，那么机器人就失去H(k+1)-E的能量值，否则它将得到E-H(k+1)的能量值。

游戏目标是到达第N个建筑，在这个过程中能量值不能为负数个单位。

现在的问题是机器人以多少能量值开始游戏，才可以保证成功完成游戏？

输入格式
第一行输入整数N。

第二行是N个空格分隔的整数，H(1),H(2),…,H(N)代表建筑物的高度。

输出格式
输出一个整数，表示所需的最少单位的初始能量值。

数据范围
1≤N,H(i)≤105,

输入样例1：
5
3 4 3 2 4
输出样例1：
4
输入样例2：
3
4 4 4
输出样例2：
4
输入样例3：
3
1 6 4
输出样例3：
3
"""

# N = int(input())
# M = list(map(int,input().split(' ')))

N = 3
M = [1, 6, 4]

def bin_search():
    """
    二分
    :return:
    """
    L = min(M)
    R = max(M)

    def check(E):
        for i in range(N):
            E = 2*E - M[i]

            # if E<M[i]:
            #     E -= M[i] - E
            # else:
            #     E += E - M[i]
            if E<0:
                return False
        return True

    while L<R:
        mid = (L+R)//2

        # 模拟
        if not check(mid):
            L = mid + 1
        else:
            R = mid

    print(L)

def fun():
    """
    逆推
    E = 2*E - M[i]
    :return:
    """
    pass

bin_search()