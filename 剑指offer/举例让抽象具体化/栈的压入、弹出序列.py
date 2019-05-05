# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        """
        使用stack模拟入栈出栈过程
        :param pushV:
        :param popV:
        :return:
        """
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            # 栈顶元素等于popV第一个元素的时候说明原来的栈在这个压到这个数的时候弹出了
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if stack:
            return False
        return True


pushV, popV = [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]
s = Solution()
print(s.IsPopOrder(pushV, popV))
