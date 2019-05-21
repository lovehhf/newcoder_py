# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
https://www.nowcoder.com/test/16723475/summary
输入为一个算数表达式的字符串。输出它经过计算之后的结果。如果该字符串不满足算数表达式则输出字符串Error。
注意：
0. 输入中的数只有非负整数。小数、负数等均需要输出Error。
1. 需要支持运算符加、减、乘以及括号。
2. 运算符的优先级为：括号>加=减>乘。
3. 支持数与操作符、操作符与操作符之间有任意空格。
3. 输入和运算过程中不需要考虑整数溢出，用32位的int即可。

输入描述:
输入1：123
输入2：1 23
输入3：1 + 2 * 3
输入4：1+(2*3)

输出描述:
输出1：123
输出2：Error
输出3：9
输出4：7

输入例子1:
1 + 2 * 3 - (4*5)

输出例子1:
-51

例子说明1:
1 + 2 * 3 - (4*5)   =>  1 + 2 * 3 - 20   => 3 * 3 - 20  =>  3 * -17  =>  -51

1+2*3+4
[1],[+]
[1,2][+] -> [3]
[3][*]
[3,3][*]
[3,3,4][*+]
[3,7][*]

1+2*3-(4*5*2)
[1][+]
[3,3][*]
[3,3][*-]
[3,3][*-(]
[3,3,4][*-(]
[3,3,4][*-(*]
[3,3,4,5][*-(*]
[3,3,4,5,2][*-(**]
"""


def computer(nums, signs):
    """
    类后缀表达式计算
    :param nums:存储运算数
    :param signs:存储运算符
    :return:
    """
    a = nums.pop()
    b = nums.pop()
    sign = signs.pop()
    nums.append(eval(str(b) + sign + str(a)))


def check(s):
    """
    检查输入合法性
    :param s:
    :return:
    """
    if s.count('(') != s.count(')'):
        return False
    return True


def solve(s):
    if not check(s):
        return "Error"
    n = len(s)
    nums = []
    signs = []
    i = 0
    while i < n:
        if s[i] == ' ':
            i += 1
            continue
        if s[i] in '(+-*':
            signs.append(s[i])
        if s[i] == ')':
            while signs and signs[-1] != '(':  # 计算出括号中所有的 *
                computer(nums, signs)
            if signs and signs[-1] == '(':  # 删掉左括号
                signs.pop()
            if signs and signs[-1] != '(':  # 括号作为一个整体与前一个数字左运算
                computer(nums, signs)
        if '0' <= s[i] <= '9':
            j = i
            while j < n and '0' <= s[j] <= '9':
                j += 1
            nums.append(int(s[i:j]))
            if signs and signs[-1] == '+':
                computer(nums, signs)
            if signs and signs[-1] == '-':
                computer(nums, signs)
            i = j - 1
        i += 1
    while len(nums) > 1 and signs:
        computer(nums, signs)
    if len(nums) == 1 and not signs:
        return nums[0]
    else:
        return "Error"


def main():
    s = input()
    print(solve(s))


def test():
    s = "(123)-4567 +4)"
    print(solve(s))
    print(solve("1 + 2 * 3 - (4*5)"))


main()
