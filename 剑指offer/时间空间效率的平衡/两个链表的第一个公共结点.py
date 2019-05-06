# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
题目描述
输入两个链表，找出它们的第一个公共结点。
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        先分别算出两条链表的长度m,n
        长的链表先走m-n步,使两条链表剩下的长度相等
        再一起走,如果有链表有相交则肯定会相等
        :param pHead1:
        :param pHead2:
        :return:
        """
        m, n = 0, 0
        p, q = pHead1, pHead2
        while p:
            m += 1
            p = p.next
        while q:
            n += 1
            q = q.next
        if m > n:
            for _ in range(m - n):
                pHead1 = pHead1.next
        if m < n:
            for _ in range(n - m):
                pHead2 = pHead2.next
        while pHead1 and pHead2:
            if pHead1 == pHead2:
                return pHead1
            pHead1, pHead2 = pHead1.next, pHead2.next
        return
