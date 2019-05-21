# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
小明是A村里的屠龙者，他一直保卫着村子的和平，以不受恶龙的侵扰。而恶龙们也对小明恨之入骨，于是恶龙们决定组织一次集体进攻，以打败小明，拿下A村。
小明知道，恶龙集体进攻的时候，会在彼此之间建立一种神秘的链接，而被这种链接连接起来的恶龙能够增长彼此的能力，
且**每有一只恶龙加入到一个链接中，这个链接里的所有龙的能力都会加1**，而只有当小明的战斗力大于龙的战斗力时，才能将龙杀死。
万幸的是，小明有一把一次性的屠龙刀，他可以无视战斗力地杀死一只龙，并消除这条龙身上的所有链接。
假设**每条龙不被链接时的战斗力为1**，**初始时所有N只恶龙被N-1条链接连接在一起**。小明想知道他**至少要有多少的战斗力，才能将所有龙都杀死，**

同时他想知道，他应该用屠龙刀杀掉哪只龙。

输入描述:
输入的第一行是一个整数N(1<=N<=40000), 表示一共有N只龙。
接下来N-1行整数对a,b（以空格分隔），表示龙之间的链接关系

输出描述:
输出以空格分隔的两个整数。第一个整数X，表示应用屠龙刀杀死的龙的编号。若有多只龙都可被屠龙刀杀死，输出编号最小的那个
第二个整数T，表示小明至少需要有的战斗力

输入例子1:
8
1 2
2 3
1 5
5 6
6 8
2 4
5 7

输出例子1:
1 5

例子说明1:
初始时所有龙都在一个链接中，此时所有龙的战斗力都为8。
当用屠龙刀杀死1号龙后，剩下的龙分别在两个链接中（2,3,4和5,6,7,8），此时5,6,7,8号龙战斗力皆为4；
2,3,4号龙的战斗力为3，故小明的战斗力至少为5才可杀死所有龙。

所有的节点连成一张图，拿掉其中一个节点 计算剩下的节点中最大的连接
"""


def dfs(num, par, graph, ans):
    cnt = 1
    for i in graph[num]:
        if i != par:
            nodeNum = dfs(i, num, graph, ans)
            cnt += nodeNum
            ans[num] = max(ans[num], nodeNum)
    ans[num] = max(ans[num], len(ans) - cnt)
    return cnt


def main():
    """
    93.3%
    :return:
    """
    n = int(input())
    if n == 1:
        print("1 0")
        return
    graph = [[] for _ in range(n)]
    ans = [0] * n
    for i in range(n - 1):
        a, b = [int(x) for x in input().split()]
        a, b = a - 1, b - 1
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    dfs(0, -1, graph, ans)
    a = min(ans)
    b = ans.index(a)
    print("%s %s" % (b + 1, a + 1))



def test():
    graph = [[1, 3, 2], [5, 0], [6, 0], [0, 4], [3], [1], [2]]
    ans = [0] * len(graph)
    dfs(0, -1, graph, ans)
    print(ans)
    a = min(ans)
    b = ans.index(a)
    print("%s %s" % (b + 1, a + 1))


main()

# def solve(n, A):
#     """
#     超时 46.67%
#     :param n:
#     :param A:
#     :return:
#     """
#
#     if n == 1:
#         return 1, 0
#     r = [set() for _ in range(n + 1)]
#     d = {}
#     # print(A)
#     B = [[] for j in range(n + 1)]
#     for i in range(n - 1):
#         a, b = A[i]
#         r[a].add(b)
#         r[b].add(a)
#     # print(r)
#     # 分别减掉1~n号点，再遍历这个点连接的其他点看其他点连接的点有多少个
#     # 这里重复遍历了太多次导致可能超时，需要记录下已经遍历过的点
#     for i in range(1, n + 1):
#         for j in r[i]:
#             visited = set()
#             visited.add(i)
#             queue = set()
#             queue.add(j)
#             while queue:
#                 cur = queue.pop()
#                 if not cur in visited:
#                     visited.add(cur)
#                     queue |= r[cur]
#             # print(visited)
#             B[i].append(len(visited) - 1)
#     # print(B[1:])
#
#     if all(len(x) > 0 for x in B[1:]):
#         C = [max(x) for x in B[1:]]
#         # print(C)
#         a = C.index(min(C)) + 1
#         b = min(C) + 1
#         return a, b
#     else:
#         return 1, 0
#
# def main():
#     A = []
#     n = int(input())
#     for i in range(n - 1):
#         a, b = [int(x) for x in input().split()]
#         A.append((a, b))
#     x, y = solve(n, A)
#     print(x, y)
#
#
# def test():
#     n = 8
#     A = [(1, 2), (2, 3), (1, 5), (5, 6), (6, 8), (2, 4), (5, 7)]
#     print(solve(n, A))
#
#
# # ans = main()
# # print(ans)
# main()
