# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2 ** d - 1) + left


class Solution:
    def getDepth(self, root):  # 计算当前树的深度
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth

    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        while root:
            left = self.getDepth(root.left)  # 左子树深度
            right = self.getDepth(root.right)  # 右子树深度
            if left == right:  # 左右子树深度相同，左子树一定是满二叉树，右子树可能为满二叉树，一定为完全二叉树
                root = root.right
                cnt += 2 ** left
            else:  # 左右子树深度不同，右子树一定是满二叉树，左子树可能为满二叉树，一定为完全二叉树
                root = root.left
                cnt += 2 ** right
        return cnt


class Solution(object):
    cnt = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root != None:
            self.cnt+=1
            self.countNodes(root.left)
            self.countNodes(root.right)
        return self.cnt