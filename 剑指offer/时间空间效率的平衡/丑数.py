# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

LeetCode 264. 丑数 II

三指针法:
一部分是丑数数组，另一部分是权重2，3，5。下一个丑数，定义为丑数数组中的数乘以权重，所得的最小值。

其一
使用三个指针idx[3]，告诉它们。比如，2应该乘以ugly[idx[0]]，即数组中的第idx[0]个值。（权重2，3，5分别对应指针，idx[0],idx[1],idx[2]）

其二
当命中下一个丑数时，说明该指针指向的丑数 乘以对应权重所得积最小。此时，指针应该指向下一个丑数。（idx[]中保存的是丑数数组下标）

其三
要使用三个并列的if让指针指向一个更大的数，不能用if-else。因为有这种情况：
丑数6，可能由于丑数2乘以权重3产生；也可能由于丑数3乘以权重2产生。
丑数10，... 等等。

 * 解题思路：
 * 因为丑数的因子只能是丑数
 * 丑数的组成成可以分成三种情况：（x和y为大于1的变量）
 * 3x,5y或3x*5y的倍数个2；可简化为丑数个2
 * （。。。。。类推）个3；可简化为丑数个3
 * （。。。。。类推）个5；可简化为丑数个5
"""


class Solution:
    def GetUglyNumber_Solution(self, n):
        ugly = [0, 1]
        idx = [1, 1, 1]  # 三指针,2,3,5的权重,表示2,3,5丑数的数量
        for i in range(1, n):
            a, b, c = ugly[idx[0]] * 2, ugly[idx[1]] * 3, ugly[idx[2]] * 5
            nextUglyNum = min(a, b, c)  # 下一个丑数
            ugly.append(nextUglyNum)
            if nextUglyNum == a:
                idx[0] += 1
            if nextUglyNum == b:
                idx[1] += 1
            if nextUglyNum == c:
                idx[2] += 1
        # print(idx)
        # print(ugly)
        return ugly[n]


s = Solution()
print(s.GetUglyNumber_Solution(100))
