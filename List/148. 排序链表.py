# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        array = []
        p = head
        while p:
            array.append(p)
            p = p.next
        array.sort(key=lambda x: x.val)
        for i in range(1, len(array)):
            array[i - 1].next = array[i]
        array[-1].next = None
        return array[0]
