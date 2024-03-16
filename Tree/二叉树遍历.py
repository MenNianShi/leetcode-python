class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#前序遍历
class Solution:
    def __init__(self):
        self.ret = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            # 前序递归
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # # 中序递归
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # 迭代1：前序遍历最常用模板（后序同样可以用）
    class Solution:
        def inorderTraversal(self,root):
            if not root:
                return []
            res = []
            stack = []
            cur = root
            while stack or cur :
                while cur :
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            return res
        def preorderTraversal(self, root) :
            if not root:
                return []
            res = []
            stack = []
            cur = root
            while stack or cur :
                while cur :
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                cur = cur.right
            return res
        def postorderTraversal(self, root) :
            if not root:
                return []
            res = []
            stack = []
            cur = root
            while stack or cur :
                while cur :
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.right
                cur = stack.pop()

                cur = cur.left
            return res[::-1]
    def preorderTraversal(self, root) :
            if not root:
                return []
            res = []
            stack = [root]
            # # 前序迭代模板：最常用的二叉树DFS迭代遍历模板
            while stack:
                cur = stack.pop()
                res.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            return res

            # # 后序迭代，相同模板：将前序迭代进栈顺序稍作修改，最后得到的结果反转
            # while stack:
            #     cur = stack.pop()
            #     if cur.left:
            #         stack.append(cur.left)
            #     if cur.right:
            #         stack.append(cur.right)
            #     res.append(cur.val)
            # return res[::-1]


    def inorderTraversal(self, root):
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res

        # # 后序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]

    def levelOrder(self, root):
        if not root:
            return []
        cur, res = [root], []
        while cur:
            lay, layval = [], []
            for node in cur:
                layval.append(node.val)
                if node.left: lay.append(node.left)
                if node.right: lay.append(node.right)
            cur = lay
            res.append(layval)
        return res




class Solution(object):
    res  = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root == None:
            return
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res
a= Solution()
root = TreeNode(1)
print(a.inorderTraversal(root))