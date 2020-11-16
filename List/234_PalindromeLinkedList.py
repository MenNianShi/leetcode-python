# Definition for singly-linked list.判断一个单链表是否是回文链
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

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



