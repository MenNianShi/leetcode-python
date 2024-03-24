# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 提前保存全部节点
# 这个方法比较简单，提前把 BST 的中序遍历结果保存到一个队列里面，当调用 next() 方法的时候，就从队列头部弹出一个元素。
#
import  collections
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0


#
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