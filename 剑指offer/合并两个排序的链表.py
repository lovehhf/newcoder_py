# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 返回合并后列表

# 递归
def Merge(self, pHead1, pHead2):
    # write code here
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    if pHead1.val > pHead2.val:
        p = pHead2
        p.next = self.Merge(pHead1, pHead2.next)
    else:
        p = pHead1
        p.next = self.Merge(pHead1.next, pHead2)
    return p


# 循环
def Merge2(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        mergeHead  =  ListNode(0)
        p = mergeHead
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                mergeHead.next = pHead2
                pHead2 = pHead2.next
            else:
                mergeHead.next = pHead1
                pHead1 = pHead1.next
            mergeHead = mergeHead.next
        if pHead1:
            mergeHead.next = pHead1
        if pHead2:
            mergeHead.next = pHead2
        return p.next