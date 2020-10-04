# # Definition for singly-linked list.
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):  # 对短的链表后面补0，若长度一样break
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        temp = ListNode(0)
        head = temp

        while l1 and l2:
            curSum = 0
            if carry:
                curSum = l1.val + l2.val + 1
            else:
                curSum = l1.val + l2.val
            if curSum > 9:
                carry = True
            else:
                carry = False

            temp.next = ListNode(curSum % 10)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
            if l1 == None and l2 == None:
                break
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
        if carry:
            temp.next = ListNode(1)
        return head.next
