# 反转从位置 m 到 n 的List。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ List长度。
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
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next # cur 和 pre 保持不变， 一步步交换 nxt 和 cur
        for _ in range(right - left):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return dummy_node.next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        def reverse(head):
            if head == None:
                return None
            if head.next == None:
                return head
            pre = head
            p = head.next
            pre.next = None
            while p != None:
                nxt = p.next
                p.next = pre
                pre = p
                p = nxt
            return pre

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        start = pre.next  # 记录起始点
        end = start
        for _ in range(right - left):
            end = end.next  # 找到结束节点
        right_node = end.next  # 记录结束点的 后一个节点，用于拼接
        left_node = pre  # 记录起始点的前一个节点，用于拼接
        # 切断链接
        left_node.next = None
        end.next = None
        x = reverse(start)  # 反转链表

        left_node.next = x
        start.next = right_node
        return dummy.next

# 92. 反转List II.py