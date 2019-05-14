# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
一个合法的圆括号表达式满足以下条件：

“”空字符串被认为是合法的。
如果字符串“X”与“Y”是合法的，则“XY”也被认为是合法的。
如果字符串“X”是合法的，则“(X)”也是合法的。
例如，“”，“()”，“()()”，“(())”这些都是合法的。

现在给出两个不保证合法的由圆括号组成的字符串，你需要交错这两个圆括号序列（在组成的新字符串中，每个初始字符串都保持原来的顺序）得到一个新的合法的圆括号表达式（不同的交错方式可能得到相同的表达式，这种情况分开计数），求共有多少结果合法的交错方式（无法得到合法的圆括号表达式则输出0），输出结果对109+7取模后的值。

输入格式
输入共两行，每行包含一个由“(”和“)”组成的字符串，长度不超过2500。

输出格式
输出为一个数字，表示合法的交错方式数量对109+7取模后的值。

输入样例：
(()
())
输出样例：
19

一个括号序列合法需要满足以下两个性质:
(记1,)记-1
1. 前缀和都>=0
2. 最后总和为0
"""


MOD = 10**9+7

def get_pre_sum(s, k):
    """
    获取括号序列的前缀和
    :param s:
    :param k:
    :return:
    """
    pre_sum = [0] * k
    for i in range(1, k):
        if s[i] == '(':
            pre_sum[i] = pre_sum[i - 1] + 1
        if s[i] == ')':
            pre_sum[i] = pre_sum[i - 1] - 1
    return pre_sum


def main(a, b):
    a, b = ' ' + a, ' ' + b
    m, n = len(a), len(b)
    sa = get_pre_sum(a, m)
    sb = get_pre_sum(b, n)
    dp = [[0] * (n) for _ in range(m)]
    dp[0][0] = 1
    if sa[-1] + sb[-1] != 0: # 总的前缀和不等于0直接返回0
        return 0
    for i in range(0, m):
        for j in range(0, n):
            if sa[i] + sb[j] >= 0:
                if i:
                    dp[i][j] += dp[i - 1][j]
                if j:
                    dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
    # for i in dp:
    #     print(i)
    return dp[m - 1][n - 1]

# a = input()
# b = input()
a = "()(()()()("
b = "(())())())"
res = main(a, b)
print(res)
