# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
给定二叉树T（树深度不超过H<=10，深度从1开始，节点个数N<1024，节点编号1~N）的层序和中序遍历，输出T从左向右叶子节点以及树先序和后序遍历序列

输入描述:
输入两行，分别代表层序和中序遍历结果，节点编号按单个空格分开

输出描述:
依次输出  从左向右叶子节点,先序,后序 遍历。节点编号按空格分开

输入例子1:
3 5 4 2 6 7 1
2 5 3 6 4 7 1

输出例子1:
2 6 1
3 5 2 4 6 7 1
2 5 6 1 7 4 3


bsf+中序
中序:左根右

先序:左根右

3 5 4 2 6 7 1
2 5 3 6 4 7 1

根节点:3 在中序中的索引:2 第一层
5：在中序中索引1<2 说明是根节点左子树
4：在中序遍历中索引4>2 说明是根节点右子树
2：在中序遍历中的索引0<1 说明是左子树的左节点
6：在中序遍历的索引为为3>2 说明在右子树且<4 说明是右子树4的左节点
7 5>4 右子树的右节点
1 

经典题 从二叉树的中序和层次遍历恢复二叉树

递归方法
从中序遍历找出左右子树，然后再从序列层次遍历中找出左右子树序列，重建二叉树
"""


class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


class Solution(object):
    def __init__(self):
        self.leaf = []

    def creatTree(self, bfsorder, inorder):
        """
        从中序遍历找出左右子树，然后再从序列层次遍历中找出左右子树序列，重建二叉树
        :param bfsorder:
        :param inorder:
        :return:
        """
        if len(bfsorder) < 1:
            return
        if len(bfsorder) == 1 and bfsorder[0] not in self.leaf:
            self.leaf.append(bfsorder[0])
            # print(self.leaf)
        root = TreeNode(bfsorder[0])
        root_index = inorder.index(root.val)  # 根节点在中序遍历的索引
        left_in = inorder[:root_index]  # 中序遍历的左子树
        right_in = inorder[root_index + 1:]  # 中序遍历的左子树
        left_bsf = [x for x in bfsorder if x in left_in]  # 层次遍历的左子树、
        right_bfs = [x for x in bfsorder if x in right_in]
        root.left = self.creatTree(left_bsf, left_in)
        root.right = self.creatTree(right_bfs, right_in)
        return root

    def preorder(self, root):
        if not root:
            return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return []
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]


from utils.TreeNode import TN2List

s = Solution()
bfsorder = [3, 5, 4, 2, 6, 7, 1]
inorder = [2, 5, 3, 6, 4, 7, 1]
root = s.creatTree(bfsorder, inorder)
pre = s.preorder(root)
post = s.postorder(root)

print(TN2List(s.creatTree(bfsorder, inorder)))
print(' '.join(list(map(str, s.leaf))))
print(' '.join(list(map(str, pre))))
print(' '.join(list(map(str, post))))
