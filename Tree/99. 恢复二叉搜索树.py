# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# Definition for a binary tree node.
# 我们需要定义3个变量分别指向3个位置：
#
# prev指向当前元素的前一个元素
# first指向要交换的第一个元素
# second指向要交换的第二个元素
# 定义prev是为了和当前元素进行比较，这个是判断元素是否逆序了的重要依据，prev只需随着遍历不断向后移动一个元素即可
#
# 总结一下，
# 我们会遇到2次当前元素小于前一元素的情况（也有可能只有一次，要交换的元素紧挨着的情况）
# 第一次遇到的时候，我们可以确定第一元素，同时我们也将第二元素设定了一个候选者（当前元素），如果没有出现第二次，那这个候选者就是第二元素；
# 如果第二次遇到，我们可以确定第二元素
# 情况是相同的，那如何判断是第一次还是第二次？
# 根据first是否赋值判断，因为第一次出现的时候，first是没有值的，而一旦fisrt赋值了，第一元素就固定了，后面只需找第二元素即可
#
# 我这里用了一个集合来存储3个标量[prev,first,second]，和直接定义3个变量意义一样，目的只是为了省去python中的nonlocal，只要明白定义的含义即可，空间复杂度依然可算作O(1)O(1)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        arr=[None,None,None]   #prev,fisrt,second
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if arr[0] and node.val<arr[0].val:
                if not arr[1]:     #第一次出现前一个元素比当前元素大
                    arr[1]=arr[0]  #确定第一元素
                arr[2]=node        #确定第二元素
            arr[0]=node            #prev随遍历向后移动
            dfs(node.right)
        dfs(root)
        arr[1].val,arr[2].val=arr[2].val,arr[1].val


# 99. 恢复二叉搜索树.py