# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
2娘和33娘接到了小电视君的扭蛋任务：
一共有两台扭蛋机，编号分别为扭蛋机2号和扭蛋机3号，22娘使用扭蛋机2号，33娘使用扭蛋机3号。
扭蛋机都不需要投币，但有一项特殊能力：
扭蛋机2号：如果塞x（x范围为>=0正整数）个扭蛋进去，然后就可以扭到2x+1个
扭蛋机3号：如果塞x（x范围为>=0正整数）个扭蛋进去，然后就可以扭到2x+2个
22娘和33娘手中没有扭蛋，需要你帮她们设计一个方案，两人“轮流扭”（谁先开始不限，扭到的蛋可以交给对方使用），
**用“最少”的次数，使她们能够最后恰好扭到N个交给小电视君。**

输入描述:
输入一个正整数，表示小电视君需要的N个扭蛋。

输出描述:
输出一个字符串，每个字符表示扭蛋机，字符只能包含"2"和"3"。

输入例子1:
10

输出例子1:
233

逆向思考,
偶数使用3号
奇数使用2号
直到为0
10=2*4+2->3号
4=2*1+1 ->3号
1=2*0+1 ->2号
"""


def helper(n, path):
    if n == 0:
        return path
    if n % 2:
        return helper((n - 1) // 2, '2' + path)
    else:
        return helper((n - 2) // 2, '3' + path)


def solve(n):
    """
    :return:
    """
    res = helper(n, '')
    print(res)


n = int(input())
solve(n)
