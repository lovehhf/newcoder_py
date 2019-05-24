# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
假设一个探险家被困在了地底的迷宫之中，要从当前位置开始找到一条通往迷宫出口的路径。
迷宫可以用一个二维矩阵组成，有的部分是墙，有的部分是路。
迷宫之中有的路上还有门，每扇门都在迷宫的某个地方有与之匹配的钥匙，只有先拿到钥匙才能打开门。
请设计一个算法，帮助探险家找到脱困的最短路径。
如前所述，迷宫是通过一个二维矩阵表示的，每个元素的值的含义如下 0-墙，1-路，2-探险家的起始位置，3-迷宫的出口
大写字母-门，小写字母-对应大写字母所代表的门的钥匙
输入描述:
迷宫的地图，用二维矩阵表示。第一行是表示矩阵的行数和列数M和N
后面的M行是矩阵的数据，每一行对应与矩阵的一行（中间没有空格）。M和N都不超过100, 门不超过10扇。
输出描述:
路径的长度，是一个整数

输入:
5 5
02111
01a0A
01003
01001

01111
输出:
7

bfs
"""


def solve(m, n, matrix):
    """
    超时  40.00%
    keys:可以走的路,捡到了钥匙将对于的门加入
    visited:走过的路,tuple,(i,j,keys)
    可以走回头路的情况是拿到了钥匙
    :param m: 行
    :param n: 列
    :param matrix: 迷宫矩阵
    :return: 最短路径数
    """
    keys = '123'
    start_i, start_j = -1, -1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '2':
                start_i, start_j = i, j
            if 'a' <= matrix[i][j] <= 'z':
                keys += matrix[i][j]
    if start_i == -1 and start_j == -1:
        return
    ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set()
    queue = [[start_i, start_j, keys, 0]]
    while queue:
        i, j, keys, step = queue.pop(0)
        if matrix[i][j] == '3':
            return step
        if 'a' <= matrix[i][j] <= 'z' and not matrix[i][j].upper() in keys:
            keys += matrix[i][j].upper()
        for dx, dy in ds:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (matrix[x][y] in keys) and not ((x, y, keys) in visited):
                visited.add((x, y, keys))
                queue.append([x, y, keys, step + 1])
    return


def solve2(m, n, matrix):
    """
    所有能优化时间的地方都用上了 还是40%
    Python不适合做这题. 改用C++
    :param m:
    :param n:
    :param matrix:
    :return:
    """
    from collections import deque
    visited = [[[0] * n for _ in range(m)] for _ in range(1024)]
    start_i, start_j = -1, -1
    for i in range(m):
        flag = False
        for j in range(n):
            if matrix[i][j] == '2':
                start_i, start_j = i, j
                flag = True
                break
        if flag:
            break
    if start_i == -1 and start_j == -1:
        return
    ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append((start_i, start_j, 0, 0, []))
    while queue:
        i, j, step, key_status, path = queue.popleft()
        if matrix[i][j] == '3':
            return step
        for dx, dy in ds:
            x = i + dx
            y = j + dy
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == '0' or visited[key_status][x][y]:
                continue
            if 'A' <= matrix[x][y] and matrix[x][y]<= 'Z':
                if  (key_status & (1 << (ord(matrix[x][y]) - ord('A')))) != 0:
                    visited[key_status][x][y] = 1
                    queue.append((x, y, step + 1, key_status, path + [(x, y)]))
            elif 'a' <= matrix[x][y] and matrix[x][y] <= 'z':
                # key_status |=
                visited[key_status][x][y] = 1
                visited[key_status | (1 << (ord(matrix[x][y]) - ord('a')))][x][y] = 1
                queue.append((x, y, step + 1, key_status | (1 << (ord(matrix[x][y]) - ord('a'))), path + [(x, y)]))
            else:
                visited[key_status][x][y] = 1
                queue.append((x, y, step + 1, key_status, path + [(x, y)]))
    return


def solve3(m, n, matrix):
    """
    空间换时间 40%
    visited 改成三维数组,省掉((x, y, keys) in visited 的判断时间
    钥匙的状态 使用二进制数表示 最多10 把钥匙 那就是1024
    比如我现在有第二把钥匙和第四把钥匙  那么我的钥匙状态就是 0101000000 也就是 320
    :param m:
    :param n:
    :param matrix:
    :return:
    """
    from collections import deque
    keys = '123'
    visited = [[[0] * n for _ in range(m)] for _ in range(1024)]
    start_i, start_j = -1, -1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '2':
                start_i, start_j = i, j
            if 'a' <= matrix[i][j] <= 'z':
                keys += matrix[i][j]
    if start_i == -1 and start_j == -1:
        return
    ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append((start_i, start_j, keys, 0, 0))
    while queue:
        i, j, keys, step, key_status = queue.popleft()
        if matrix[i][j] == '3':
            return step
        if 'a' <= matrix[i][j] <= 'z' and not matrix[i][j].upper() in keys:
            keys += matrix[i][j].upper()
            key_status += 1 << (ord(matrix[i][j]) - ord('a'))
        for dx, dy in ds:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (matrix[x][y] in keys) and not visited[key_status][x][y]:
                visited[key_status][x][y] = 1
                queue.append((x, y, keys, step + 1, key_status))
    return


def main():
    matrix = []
    m, n = [int(x) for x in input().split()]
    for i in range(m):
        matrix.append(input())
    print(solve(m, n, matrix))
    print(solve2(m, n, matrix))


def test():
    m, n = 5, 5
    matrix = ['02111',
              '01a0A',
              '01003',
              '01001',
              '01111']
    print(solve(m, n, matrix))
    print(solve2(m, n, matrix))
    print(solve3(m, n, matrix))


test()
