# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
import collections

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        return self.levelOrder(root)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = [root]
        ans = []
        if not root:
            return None
        while len(level) > 0:
            next_level = []
            cur_level = []
            n = len(level)
            for i in range(n - 1):
                level[i].next = level[i + 1]
            for node in level:
                cur_level.append(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ans.append(cur_level)
            level = next_level
        return root
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

            # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:
            cur_len = len(Q)
            for i in range(cur_len):
                cur = Q.popleft()
                if i < cur_len - 1:
                    cur.next = Q[0]
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)
        return root

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

            # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:
            cur_len = len(Q)
            next_level = collections.deque([])
            for i in range(cur_len):
                cur = Q.popleft()
                if len(Q)>0:
                    cur.next = Q[0]
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            Q = next_level

        return root