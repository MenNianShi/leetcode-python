# 聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#
# Definition for a binary tree node.

# 我们可以用 f(o)f(o) 表示选择 oo 节点的情况下，oo 节点的子树上被选择的节点的最大权值和；g(o)g(o) 表示不选择 oo 节点的情况下，oo 节点的子树上被选择的节点的最大权值和；ll 和 rr 代表 oo 的左右孩子。
#
# 当 oo 被选中时，oo 的左右孩子都不能被选中，故 oo 被选中情况下子树上被选中点的最大权值和为 ll 和 rr 不被选中的最大权值和相加，即 f(o) = g(l) + g(r)f(o)=g(l)+g(r)。
# 当 oo 不被选中时，oo 的左右孩子可以被选中，也可以不被选中。对于 oo 的某个具体的孩子 xx，它对 oo 的贡献是 xx 被选中和不被选中情况下权值和的较大值。故 g(o) = \max \{ f(l) , g(l)\}+\max\{ f(r) , g(r) \}g(o)=max{f(l),g(l)}+max{f(r),g(r)}。
# 至此，我们可以用哈希映射来存 ff 和 gg 的函数值，用深度优先搜索的办法后序遍历这棵二叉树，我们就可以得到每一个节点的 ff 和 gg。根节点的 ff 和 gg 的最大值就是我们要找的答案。
#
# 我们可以做一个小小的优化，我们发现无论是 f(o)f(o) 还是 g(o)g(o)，他们最终的值只和 f(l)f(l)、g(l)g(l)、f(r)f(r)、g(r)g(r) 有关，所以对于每个节点，我们只关心它的孩子节点们的 ff 和 gg 是多少。我们可以设计一个结构，表示某个节点的 ff 和 gg 值，在每次递归返回的时候，都把这个点对应的 ff 和 gg 返回给上一级调用，这样可以省去哈希映射的空

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        self.f = {None:0}
        self.g = {None:0}
        self.dfs(root)
        return max(self.f[root], self.g[root])

    def dfs(self, o):
        if o == None:
            return
        self.dfs(o.left)
        self.dfs(o.right)
        self.f[o] = o.val + self.g[o.left] + self.g[o.right]
        self.g[o] = max(self.f[o.left], self.g[o.left]) + max(self.f[o.right], self.g[o.right])


class Solution(object):
    def rob(self, root):
        x = self.dfs(root)
        return max(x[0], x[1])

    def dfs(self, o):
        if o == None:
            return (0, 0)
        left = self.dfs(o.left)
        right = self.dfs(o.right)
        selected = o.val + left[1] + right[1]
        not_selected = max(left[0], left[1]) + max(right[0], right[1])
        return (selected, not_selected)