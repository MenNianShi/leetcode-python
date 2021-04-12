# Definition for a binary tree node.
# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
#
# 2
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):

    def longestUnivaluePath(self, root):
        self.ans = 0
        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length+1
            if node.right and node.right.val == node.val:
                right_arrow= right_length+1
            self.ans = max(self.ans,left_arrow+right_arrow)
            return max(left_arrow,right_arrow)
        arrow_length(root)
        return self.ans


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        longpaths = []

        def getLongest(node, parent_val):
            if node is None: return 0
            if node.val == parent_val:
                return (max(getLongest(node.left, node.val), getLongest(node.right, node.val)) + 1)
            else:
                longpaths.append(getLongest(node.left, node.val)
                                 + getLongest(node.right, node.val))
                return 0

        getLongest(root, None)
        return max(longpaths) if longpaths else 0