class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1000, head)
        pre = dummy
        while pre.next:
            cur = pre.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            # 不相等说明需要删除 val =  cur.val 的 节点
            if cur != pre.next:
                pre.next = cur.next
            # 相等说明，cur是不重复节点
            else:
                pre = pre.next
        return dummy.next
# 82. 删除排序链表中的重复元素 II




