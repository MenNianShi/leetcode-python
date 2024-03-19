# 给定一个单List L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定List 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定List 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
# Definition for singly-linked list.
# 注意到目标List即为将原List的左半端和反转后的右半端合并后的结果。
#
# 这样我们的任务即可划分为三步：
#
# 找到原List的中点（参考「876. List的中间结点」）。
#
# 我们可以使用快慢指针来 O(N)O(N) 地找到List的中间节点。
# 将原List的右半端反转（参考「206. 反转List」）。
#
# 我们可以使用迭代法实现List的反转。
# 将原List的两端合并。
#
# 因为两List长度相差不超过 11，因此直接合并即可。

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):#超时
    def reorderList(self, head):
        if head==None or head.next==None or head.next.next==None :
            return
        p = head.next
        q = self.getlastpre(head)
        head.next = q.next
        q.next = None
        self.reorderList(p)
        head.next.next = p
    def getlastpre(self,p):
        while p.next.next:
            p = p.next
        return p
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:
            #find mid
            fast, slow = head, head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            head1 = head
            head2 = slow.next
            slow.next = None

            # reverse linked list head2
            dummy = ListNode(0)
            dummy.next = head2
            p = head2.next
            head2.next = None
            while p:
                temp = p
                p = p.next
                temp.next = dummy.next
                dummy.next = temp
            head2 = dummy.next

            # merge two linked list head1 and head2
            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2
class Solution:
    def reorderList(self, head):
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head) :
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1, l2):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp


# 143. 重排List.py