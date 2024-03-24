class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        level = [root]
        while len(level) > 0 :
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return root
# 117. 填充每个节点的下一个右侧节点指针 II.py