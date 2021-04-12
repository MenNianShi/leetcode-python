# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):

    res = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root==None : return 0
        self.pathSum(root.left,sum)
        self.pathSum(root.right,sum)
        self.helper(root,sum)
        return self.res
    def helper(self,root,sum):

        if root==None : return
        if sum-root.val==0 : self.res+=1
        self.helper(root.left,sum-root.val)
        self.helper(root.right, sum - root.val)


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        return self.pathSdicts(root, sum, {0: 1}, 0)

    def pathSdicts(self, root, sum, dicts, cur):
        if not root:
            return 0

        count = 0
        cur += root.val

        if cur - sum in dicts:
            count += dicts[cur - sum]

        if cur in dicts:
            dicts[cur] += 1
        else:
            dicts[cur] = 1

        l = self.pathSdicts(root.left, sum, dicts, cur)
        r = self.pathSdicts(root.right, sum, dicts, cur)

        count = count + l + r
        dicts[cur] -= 1  # 算右边数之前要把它减掉

        return count
