# 记给定链表的长度为 nn，注意到当向右移动的次数 k \geq nk≥n 时，我们仅需要向右移动 k%n 次即可。因为每 nn 次移动都会让链表变为原状。这样我们可以知道，新链表的最后一个节点为原链表的第 (n - 1) - (k mod n) 个节点（从 00 开始计数）。
#
# 这样，我们可以先将给定的链表连接成环，然后将指定位置断开。
#
# 具体代码中，我们首先计算出链表的长度 n，并找到该链表的末尾节点，将其与头节点相连。这样就得到了闭合为环的链表。然后我们找到新链表的最后一个节点（即原链表的第 (n - 1) - (k mod n)个节点），将当前闭合为环的链表断开，即可得到我们所需要的结果。
#
# 特别地，当链表长度不大于 1，或者 k 为 n 的倍数时，新链表将与原链表相同，我们无需进行任何处理
#

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        add = n - k % n
        if add == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret
# 61. 旋转链表.py