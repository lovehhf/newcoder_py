# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""


def Mirror(self, root):
    # write code here
    if root:
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)