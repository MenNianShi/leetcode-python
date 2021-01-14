class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None or fast.next==None:
            return None
        slow = head
        while fast != slow :
            fast= fast.next
            slow=slow.next
        return slow


class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    def detectCycle(self, pHead):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        low = self.hasCycle(pHead)
        if low==None:
            return None
        #如果走出上面这个循环说明有环，且fast = slow
        fast=pHead
        #找出环的入口
        while low!=fast:
            low=low.next
            fast=fast.next
        return fast