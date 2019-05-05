# -*- coding:utf-8 -*-

__author__ = 'huanghf'
"""
题目描述
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""
from utils.TreeNode import List2TN


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        def dfs(root, path, s, res):
            if not root:
                return
            # 叶子节点
            if not root.left and not root.right:
                # res.append(path + [root.val])
                if s + root.val == expectNumber:
                    res.append(path + [root.val])
                return
            dfs(root.left, path + [root.val], s + root.val, res)
            dfs(root.right, path + [root.val], s + root.val, res)

        res = []
        dfs(root, [], 0, res)
        res = sorted(res,key=lambda x:len(x),reverse=True)
        return res


root = List2TN([1, 6, 3, None, None, 6, 3])
s = Solution()
print(s.FindPath(root, 7))
