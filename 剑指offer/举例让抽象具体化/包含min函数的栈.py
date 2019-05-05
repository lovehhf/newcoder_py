# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""

class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if not self.minStack:
            self.minStack.append(node)
        else:
            if self.minStack[-1] > node:
                self.minStack.append(node)

    def pop(self):
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]