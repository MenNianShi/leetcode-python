# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.dummy = ListNode(0, None)
        self.head = ListNode(0, None)
        self.dummy.next = self.head
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            node = ListNode(cur.val, None)
            self.head.next = node
            self.head = self.head.next
            cur = cur.right
        self.p = self.dummy.next

    def next(self):
        """
        :rtype: int
        """
        self.p = self.p.next
        return self.p.val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p.next:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# 173. 二叉搜索树迭代器.py