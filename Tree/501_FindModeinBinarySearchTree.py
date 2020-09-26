# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.count = 0

        def dfs(node, last_node, last_count):
            if not node:
                return last_node, last_count

            last_node, last_count = dfs(node.left, last_node, last_count)

            if last_node and last_node.val == node.val:
                last_count = last_count + 1
            else:
                last_count = 1

            if last_count == self.count:
                self.result.append(node.val)
            elif last_count > self.count:
                self.count = last_count
                self.result = [node.val]

            return dfs(node.right, node, last_count)

        dfs(root, None, 0)
        return self.result

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        occur = {}
        level = [root]

        while level:
            next_level = []
            for node in level:
                if node.val in occur:
                    occur[node.val] += 1
                else:
                    occur[node.val] = 1

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level

        max_val = max(occur.values())
        for k, v in occur.iteritems():
            if v == max_val:
                res.append(k)

        return res