# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head
        :rtype: TreeNode
        """
        s = []
        while head!=None :
            s.append(head.val)
            head = head.next
        return self.buildTree(s)
    def buildTree(self,s):
        if len(s)==0:
            return None
        mid = len(s)//2
        root = TreeNode(s[mid])
        root.left = self.buildTree(s[:mid])
        root.right = self.buildTree(s[mid+1:])
        return root


class Solution:
    def sortedListToBST(self, head):
        def getMedian(left, right) :
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left, right) :
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)

