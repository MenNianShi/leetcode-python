# Definition for singly-linked list. 先反转，再加，在反转
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2): # 栈后进先出
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 , s2 = [] ,[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry!= 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        return self.reverseList(self.addTwoNumbers2(l1, l2))

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
        p = head.next
        pre.next = None
        while p != None:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
        return pre

    def addTwoNumbers2(self, l1, l2):
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

# 445. 两数相加 II.py