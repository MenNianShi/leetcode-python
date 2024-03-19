# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre != None:
            self.swapPair(pre)
            if pre.next:
                pre = pre.next.next
            else:
                break
        return dummy.next

    def swapPair(self, head):
        # 交换接下来两个节点
        if head.next and head.next.next:
            q = head.next
            p = head.next.next
            nxt = p.next
            head.next = p
            p.next = q
            q.next = nxt
        return head

# 24. 两两交换链表中的节点.py