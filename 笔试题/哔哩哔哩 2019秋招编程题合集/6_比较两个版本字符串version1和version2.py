# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
如果version1 > version2 返回1，如果 version1 < version2 返回-1，不然返回0.

输入的version字符串非空，只包含数字和字符.。.字符不代表通常意义上的小数点，只是用来区分数字序列。
例如字符串2.5并不代表二点五，只是代表版本是第一级版本号是2，第二级版本号是5.


输入描述:
两个字符串，用空格分割。
每个字符串为一个version字符串，非空，只包含数字和字符.

输出描述:
只能输出1, -1，或0

输入例子1:
0.1 1.1

输出例子1:
-1
"""


def solve(version1, version2):
    v1, v2 = version1.split('.'), version2.split('.')
    v1 = list(map(int,v1))
    v2 = list(map(int,v2))
    while v1 and v2:
        a, b = v1.pop(0), v2.pop(0)
        if a < b:
            return -1
        elif a > b:
            return 1
    if v1 and any(x!=0 for x in v1):
        return 1
    if v2 and any(x!=0 for x in v2):
        return -1
    return 0


version1, version2 = input().split()
res = solve(version1,version2)
print(res)