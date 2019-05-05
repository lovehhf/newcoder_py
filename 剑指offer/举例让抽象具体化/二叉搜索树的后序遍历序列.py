# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。


BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），
如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。

算法步骤如下：
1. 找到根结点；
2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；若出现小于根结点的元素，则直接返回false；若右侧全都大于根结点，则：
4. 分别递归判断左/右子序列是否为后序序列；
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 左右根
        # 通过根节点找到左右子树 在再递归判断左右
        def check(ls):
            if not ls:
                return True
            n = len(ls)
            root = ls[-1]
            i = 0
            while i < n and ls[i] < root:
                i += 1
            for j in range(i,n-1):
                if ls[j] < root:
                    return False
            return check(ls[:i]) and check(ls[i:-1])

        if not sequence:
            return False
        res = check(sequence)
        return res




    # def VerifySquenceOfBST2(self, sequence):
    #     # write code here
    #     if sequence == None or len(sequence) == 0:
    #         return False
    #     length = len(sequence)
    #     root = sequence[length - 1]
    #     # 在二叉搜索 树中 左子树节点小于根节点
    #     for i in range(length):
    #         if sequence[i] > root:
    #             break
    #     # 二叉搜索树中右子树的节点都大于根节点
    #     for j in range(i, length):
    #         if sequence[j] < root:
    #             return False
    #     # 判断左子树是否为二叉树
    #     left = True
    #     if i > 0:
    #         left = self.VerifySquenceOfBST2(sequence[0:i])
    #     # 判断 右子树是否为二叉树
    #     right = True
    #     if i < length - 1:
    #         right = self.VerifySquenceOfBST2(sequence[i:-1])
    #     return left and right


s = Solution()
sequence = [7,4,6,5]

print(s.VerifySquenceOfBST(sequence))
