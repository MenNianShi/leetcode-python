# Definition for a binary tree node.

import queue
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        q = queue.Queue()
        q.put(root)
        while(q.empty()==False):
            n = q.qsize()
            mysum = 0
            for i in range(0,n):
                x= q.get()
                mysum +=x.val
                if x.left!=None: q.put(x.left)
                if x.right!=None: q.put(x.right)
            result.append(mysum/n)
        return result

b = TreeNode(3)
c = TreeNode(9)
d = TreeNode(20)
e = TreeNode(15)
f = TreeNode(7)
b.left = c
b.right = d
d.left = e
d.right =f
a = Solution()
print(a.averageOfLevels(b))
