# 将二叉树展开为单链表之后，单链表中的节点顺序即为二叉树的前序遍历访问各节点的顺序。因此，可以对二叉树进行前序遍历，获得各节点被访问到的顺序。由于将二叉树展开为链表之后会破坏二叉树的结构，因此在前序遍历结束之后更新每个节点的左右子节点的信息，将二叉树展开为单链表。
#


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root != None:
            if root.left == None:
                # 左子树为 null，直接考虑下一个节点
                root = root.right
            else :
                # 找左子树最右边的节点
                pre = root.left
                while pre.right != None:
                    pre = pre.right
                # 将原来的右子树接到左子树的最右边节点
                pre.right = root.right
                # 将左子树插入到右子树的地方
                root.right = root.left
                root.left = None
                # 考虑下一个节点
                root = root.right



class Solution:
    def flatten(self, root):
        preorderList = list()
        stack = list()
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr


