# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""
from utils.TreeNode import TreeNode, List2TN


class Solution:
    def IsBalanced_Solution(self, pRoot):
        """
        平衡术的子树也都是平衡二叉树
        :param pRoot:
        :return:
        """

        def get_depth(root):
            """
            获取二叉树深度
            :param root:
            :return:
            """
            if not root:
                return 0
            return max(get_depth(root.left), get_depth(root.right)) + 1

        if not pRoot:
            return True
        if abs(get_depth(pRoot.left) - get_depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    # def IsBalanced_Solution2(self, pRoot):
    #     """
    #     上面的做法有很明显的问题，在判断上层结点的时候，会多次重复遍历下层结点，增加了不必要的开销。
    #     如果改为从下往上遍历，如果子树是平衡二叉树，则返回子树的高度；如果发现子树不是平衡二叉树，则直接停止遍历，这样至多只对每个结点访问一次。
    #     :param pRoot:
    #     :return:
    #     """
    #
    #     def getDepth(root):
    #         if not root:
    #             return 0
    #         left = getDepth(root.left)
    #         if left == -1:
    #             return -1
    #         right = getDepth(root.right)
    #         if root.right == -1:
    #             return -1
    #         print(root,left,right,abs(left - right))
    #         if abs(left - right) > 1:
    #             print("SBSBBSBSBSB")
    #             return -1
    #         else:
    #             return max(left, right) + 1
    #         # return -1 if abs(left - right) > 1 else max(left, right) + 1
    #     return getDepth(pRoot) != -1


root = List2TN([1, None, 2, None, 3, None, 4, None, 5])
s = Solution()
print(s.IsBalanced_Solution(root))
