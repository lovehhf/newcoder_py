# -*- coding:utf-8 -*-

__author__ = 'huanghf'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        # 利用队列进行遍历，先进先出
        l = []
        if not root:
            return []
        q = [root]
        while len(q):
            # 将队列中的第一个元素取值并出队列
            t = q.pop(0)
            l.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return l