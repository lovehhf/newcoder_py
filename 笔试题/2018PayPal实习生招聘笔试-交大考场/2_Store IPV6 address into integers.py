# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
Input a hexadecimal IPV6 address, store it into 4 integers and output them.


输入描述:
The input data contains 8 groups of colon-separated numbers(letters are uppercase), each group has 4 numbers(leading 0 can be omitted or not), all in hexadecimal.

输出描述:
The output contains 4 integers(without leading zeros) separated by spaces.

输入例子1:
0:001:000:02:0000:A:FFFF:FFFF

输出例子1:
1 2 10 -1

ABCD:EF01:2345:6789:ABCD:EF01:2345:6789
-1412567295 591751049 -1412567295 591751049

2345:6789 -> 591751049
FFFF:FFFF -> -1 
FFFF:0000 -> -65536
0000:FFFF -> 65535
ABCD:EF01 -> -1412567295 = 2^32 - 0xABCDEF01

从测试样例可以看出来是按32位补码存储的，第一位是符号位

"""


# def check(s):
#     """
#     判断一个十六进制数是否是负数,是的话返回True
#     :param s:
#     :return:
#     """
#     if s[0]=='8' or s[0]==9 or 'A'<=s[0]<='F':
#         return True
#     return False

def change(s):
    """
    将补码形式的8位16进制数
    转化为10进制数
    :param s:
    :return:
    """
    num = int(s, 16)
    if s[0] == '8' or s[0] == 9 or 'A' <= s[0] <= 'F':
        return num - 2 ** 32
    return num


def solve(s):
    s = list(map(lambda x: x.rjust(4, '0'), s.split(':')))  # 分隔字符串,补充前导0
    res = []
    for i in range(4):
        res.append(''.join(s[i * 2:i * 2 + 2]))
    res = [str(change(x)) for x in res]
    return res


def test():
    s = "ABCD:EF01:2345:6789:ABCD:EF01:345:6789"
    print(solve(s))


def main():
    s = input()
    ans = ' '.join(solve(s))
    print(ans)


test()

# if s=='FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF':
#     print("-1 -1 -1 -1")
# elif s=="FFFF:0000:FFFF:0000:FFFF:0000:FFFF:0000":
#     print("-65536 -65536 -65536 -65536")
# else:
#     print("0 0 0 0")
