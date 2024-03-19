class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self , head ):
        # write code here
        dummy = ListNode(0)
        cur = dummy
        pre = dummy
        pre_val = float('-inf')
        while head :
            if head.val != pre_val:
                pre = cur
                cur.next = head
                cur = cur.next
                pre_val = head.val
            else:
                cur = pre
                cur.next = None
            head = head.next
        cur.next = None
        return dummy.next


class Solution:
    def deleteDuplicates(self, head):
        # write code here
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        pre = dummy
        pre_val = float('-inf')
        nums = []
        while head:
            if pre.val == head.val:
                nums.append(head.val)
                pre.next = head.next
                head = head.next

            else:
                pre = pre.next
                head = head.next
        head = dummy.next
        pre = dummy
        while head:
            if head.val in nums:
                pre.next = head.next
                head = head.next

            else:
                pre = pre.next
                head = head.next
        return dummy.next
a = Solution()
b = ListNode(1)
c = ListNode(1)
b.next = c

print(a.deleteDuplicates(b))
# 删除有序链表中重复出现的元素.py