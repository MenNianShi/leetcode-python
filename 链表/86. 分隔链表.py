# 86. 分隔链表
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        pre = dummy
        while pre.next and pre.next.val < x:
            pre = pre.next
        # 找到第一个  >= x 的数  pre.next
        cur = pre
        while cur.next:
            if cur.next.val < x:
                # cur.next 需要前移d到 pre之后， pre.next 永远指向第一个>=x的数
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                pre = pre.next
            else:
                cur = cur.next

        return dummy.next



