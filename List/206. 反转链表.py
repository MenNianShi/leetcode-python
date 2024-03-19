# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head ==None:
            return None
        if head.next ==None:
            return  head
        pre =head
        p = head.next
        pre.next = None
        while p!=None:
            nxt = p.next
            p.next = pre
            pre  =p
            p=nxt
        return pre
# 206. 反转链表.py