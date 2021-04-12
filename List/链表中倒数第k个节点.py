class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here
        dummy = ListNode(0)
        dummy.next = pHead
        slow = fast = dummy
        for i in range(k):
            if fast:
                fast = fast.next

        if fast == None:
            return None
        while fast != None:
            fast = fast.next
            slow = slow.next
        return slow