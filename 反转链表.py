# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
输入一个链表，反转链表后，输出新链表的表头。
"""



# 返回ListNode
def ReverseList(self, pHead):
    # write code here
    # 链表为空活或者链接只有一个元素 直接返回
    if not pHead or not pHead.next:
        return pHead
    """

    用三个指针分别指向当前、前一个、后一个，每次循环使当前节点的next指针指向前一个（原指向后一个），然后依次向后平移三个指针（注意移动的先后次序）。
    其实可以节省一个指向新链表头的指针，循环体如下便可：
        while (cur)
        {
            next = cur->next; // 备份，以免链表断裂
    
            cur->next = pre; // 反转
    
            pre = cur; // 平移
            cur = next;        
        }
        return pre;
    最终需要返回pre，因为cur已经变成原链表中最后的那个空指针了。
    
    https://blog.csdn.net/feliciafay/article/details/6841115
    """
    p = pHead
    q = pHead.next
    pHead.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p

    # reversedHead = None
    #
    # while pHead:
    #     tmp = pHead.next
    #     pHead.next = reversedHead
    #     reversedHead = pHead
    #     pHead = tmp
    # return reversedHead
