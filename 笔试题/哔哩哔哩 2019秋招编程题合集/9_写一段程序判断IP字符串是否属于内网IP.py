# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
时间限制：1秒

空间限制：32768K

从业 666 年的 BILIBILI 网络安全工程师 KindMo 最近很困惑，公司有一个业务总是受到 SSRF 攻击。请帮他写一个程序，判断输入的字符串是否属于内网IP，用于防御该漏洞。
我们知道常见的内网IP有，127.0.0.1，192.168.0.1 等。

输入描述:
每次输入仅包含一个IP字符串，即一个测试样例

输出描述:
对于每个测试实例输出整数1或0，1代表True，即输入属于内网IP，0代表False，即输入不属于内网IP或不是IP字符串。

输入例子1:
42.96.146.169

输出例子1:
0
"""


def check(s):
    if s == '127.0.0.1':
        return 1
    ip = [int(x) for x in s.split('.')]
    if len(ip)==4:
        if ip[0]==10 and all(0<=x<=255 for x in range(1,4)):
            return 1
        if ip[0]==192 and ip[1]==168 and 0<=ip[2]<=255 and 0<=ip[3]<=255:
            return 1
        if ip[0]==172 and 16<=ip[1]<=31 and 0<=ip[2]<=255 and 0<=ip[3]<=255:
            return 1
    return 0

s = input()
res = check(s)
print(res)