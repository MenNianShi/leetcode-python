# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
     def removeElements(self, head, val):
         """
         :type head: ListNode
         :type val: int
         :rtype: ListNode
         """
         dummy = ListNode(0)
         dummy.next = head

         prev = dummy
         curr = dummy.next
         while curr is not None:
             if curr.val == val:
                 prev.next = curr.next
             else:
                 prev = curr
             curr = curr.next

         return dummy.next
# 题目没有要求不改变节点的值，那么可以定义快慢两个指针，在快指针遍历链表的时候，
# 将不等于val值的节点的值赋给慢指针指向的节点。
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        slow, fast = new_head, head
        while fast:
            if fast.val != val:
                slow.next.val = fast.val
                slow = slow.next
            fast = fast.next
        slow.next = None
        return new_head.next
#递归
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next

        return head

# 203. 移除链表元素.py