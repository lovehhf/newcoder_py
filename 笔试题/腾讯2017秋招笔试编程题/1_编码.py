# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，
形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy 
其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.

输入描述:
输入一个待编码的字符串,字符串长度小于等于100.

输出描述:
输出这个编码的index

输入例子1:
baca

输出例子1:
16331

https://blog.csdn.net/Shayne_S/article/details/80243068

baca = 25**3+25**2+25+1 + 2*(25+1) + 3
caca = 2*(25**3+25**2+25+1) + 2*(25+1) + 3 
cccb = 3*(25**3+25**2+25+1) + 2*(25**2+25+1) + 2*(25+1) + 1 +3
"""

def fun(s):
    key_list = [chr(ord('a')+x) for x in range(0,25)]
    value_list = list(range(0,25))
    dic = dict(zip(key_list,value_list))
    n = len(s)
    s = s.ljust(4,'a')
    res = dic[s[0]]*(25**3+25**2+25+1) + dic[s[1]]*(25**2+25+1) + dic[s[2]]*(25+1) + dic[s[3]] + n-1

    # res = 0
    # if n==4:
    #     res = dic[s[0]]*(25**3+25**2+25+1) + dic[s[1]]*(25**2+25+1) + dic[s[2]]*(25+1) + dic[s[3]] + 3
    # if n == 3:
    #     res = dic[s[0]]*(25**3+25**2+25+1) + dic[s[1]]*(25**2+25+1) + dic[s[2]]*(25+1) + 2
    # if n == 2:
    #     res = dic[s[0]] * (25 ** 3 + 25 ** 2 + 25 + 1) + dic[s[1]] * (25 ** 2 + 25 + 1) + 1
    # if n == 1:
    #     res = dic[s[0]] * (25 ** 3 + 25 ** 2 + 25 + 1)

    return res

print(fun('b'))
# s = input()
