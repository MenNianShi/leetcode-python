# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # 迭代版，时间复杂度O(n)，空间复杂度O(1)
        # Need help
        if head == None: return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy  # start =0.   Given this linked list: 1->2->3->4->5    #    For k = 2, you should return: 2->1->4->3->5
        while start.next:
            end = start  # end = 0
            for i in range(k - 1):
                end = end.next  # end = 1
                if end.next == None: return dummy.next
            (start.next, start) = self.reverse(start.next,
                                               end.next)  # (start.next=3, start=1)=self.reverse(start.next=1, end.next=2)
        return dummy.next

    def reverse(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
            # start.next, start.next.next, dummy.next = start.next.next, dummy.next, start.next
            # The above line is wrong! But WHY?
        return (end, start)
