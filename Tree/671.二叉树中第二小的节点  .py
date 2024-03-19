# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
#
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
# Input:
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# Example 2:
# Input:
#     2
#    / \
#   2   2
#
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution(object):#遍历二叉树，记录比根节点大的所有节点中值最小的元素
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0x80000000
        minVal = root.val
        def traverse(root):
            if not root: return
            if self.ans > root.val > minVal:
                self.ans = root.val
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.ans if self.ans != 0x80000000 else -1
class Solution(object):
    l=[]
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mid(root)
        a = set(self.l)
        if len(a)<2:
            return -1
        maxA = max(a)
        a.remove(maxA)
        return max(a)
    def mid(self,root):
        if root ==None:
            return
        self.mid(root.left)
        self.l.append(root.val)
        self.mid(root.right)
a = TreeNode(2)
b = TreeNode(2)
c = TreeNode(2)
a.left = b
a.right = c
exa = Solution()
print(exa.findSecondMinimumValue(a))
# 671.二叉树中第二小的节点  .py