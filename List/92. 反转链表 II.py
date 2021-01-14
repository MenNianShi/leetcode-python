# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    successor = None
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==1:
            return self.reverseN(head,n)
        head.next  = self.reverseBetween(head.next,m-1,n-1)
        return head
    #反转前N个
    def reverseN(self, head, n):
        if (n==1):
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head
        # 以head.next为起点，需要反转前n - 1 个节点
        last = self.reverseN(head.next,n-1)
        head.next.next = head
        head.next = self.successor
        return last
