# Definition for singly-linked list.判断一个单List是否是回文链
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head.next
        x = ListNode(head.val)
        x_head = x
        while p:
            x.next = ListNode(p.val)
            p = p.next
            x = x.next
        x = self.reverseList(x_head)
        res = True
        while x and head:
            if x.val != head.val:
                res = False
            x = x.next
            head = head.next
        return res

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head

        pre = head
        head = head.next
        pre.next = None
        while head != None:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre



class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        left_end = self.end_of_first_half(head)
        right_part =self.reverse_list(left_end.next)

        a = head
        b = right_part
        while b :
            if a.val != b.val:
                return False
            else:
                a = a.next
                b = b.next
        return True
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
# 234. 回文List.py