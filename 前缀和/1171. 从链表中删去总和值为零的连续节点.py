#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 给你一个List的头节点head，请你编写代码，反复删去List中由总和值为0的连续节点组成的序列，直到不存在这样的序列为止。
#
# 删除完毕后，请你返回最终结果List的头节点。
#
# 你可以返回任何满足题目要求的答案。
#
# （注意，下面示例中的所有序列，都是对ListNode对象序列化的表示。）
#
# 示例
# 1：
#
# 输入：head = [1, 2, -3, 3, 1]
# 输出：[3, 1]
# 提示：答案[1, 2, 1]
# 也是正确的。
# 示例
# 2：
#
# 输入：head = [1, 2, 3, -3, 4]
# 输出：[1, 2, 4]
# 示例
# 3：
#
# 输入：head = [1, 2, 3, -3, -2]
# 输出：[1]
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head :
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head = dummy
        prefix = 0
        while head :
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next
# 1171. 从List中删去总和值为零的连续节点.py