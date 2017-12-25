# Definition for singly-linked list.判断一个单链表是否是回文链
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        tmp_list = []
        while head:
            tmp_list.append(head.val)
            head = head.next
        length = len(tmp_list)
        for i in range(0,length/2):
            if tmp_list[i] != tmp_list[length-i-1]:
                return False
        return True
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a == a[::-1]
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow.next = reversed(slow.next)
            slow  = slow.next
        else:
            slow = reversed(slow)
        while slow:
            if head.val != slow.val:
                return  False
            slow = slow.next
            head = head.next
        return True