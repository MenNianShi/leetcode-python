# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        p = head
        while p:
            length+=1
            p = p.next
        rm_k  = length - n + 1
        p = ListNode(0)
        x = p
        p.next = head
        m = 0
        while m!=rm_k-1:
            m+=1
            p = p.next
        if p.next:
            p.next = p.next.next
        else:
            p.next = None
        return x.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
# a.next = b
# b.next = c
# c.next =d
# d.next = e
z = Solution()
print(z.removeNthFromEnd(a,1))