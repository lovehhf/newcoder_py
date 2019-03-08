# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False

        # 空数直接返回False
        if not pRoot1 or not pRoot2:
            return False
        # 根节点是否对的上
        if pRoot1.val == pRoot2.val:
            # 以这个根节点为为起点判断是否包含Tree2
            result = self.DoesHaveTree2(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesHaveTree2(self, tree_1, tree_2):
        # 树2遍历完了对的上 则返回True
        if tree_2 == None:
            return True
        # 树1先遍历完了 返回False
        if tree_1 == None:
            return False
        # 只要其中一个节点对不上,返回False
        if tree_1.val != tree_2.val:
            return False
        # 如果根节点对应的上，就去比对左右子树
        return self.DoesHaveTree2(tree_1.left, tree_2.left) and self.DoesHaveTree2(tree_1.right, tree_2.right)
