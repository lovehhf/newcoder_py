# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个链表，输出该链表中倒数第k个结点。
"""


class Solution:
    def FindKthToTail(self, head, k):
        #代码思路：两个指针，都先指向头结点，然后让第一个指针走k-1步；到达第k个节点，
        #然后两个指针同时往后移，当第一个节点到达末尾的时候，第二个节点所在位置就是倒数第k个节点了
        front = head
        later = head
        for i in range(k):
            if front==None:
                return None
            if front.next == None and i==k-1:
                return head
            front = front.next
        while front.next !=None:
            front = front.next
            later = later.next
        return later.next