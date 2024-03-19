# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
#
# 返回的长度需要从小到大排列。
#
# 示例：
#
# 输入：
# shorter = 1
# longer = 2
# k = 3
# 输出： {3,4,5,6}
# 提示：
#
# 0 < shorter <= longer
# 0 <= k <= 100000
# 两个特例：
#
# k == 0，这个时候返回 []
# shorter == longer，此时结果中只有一种长度，即 shorter * k
# 除了上述两种特例之外，即要从长度为 shorter 和 longer 的木板中（longer > shorter），挑选 k (k > 0) 个。
#
# 先说结论：构成的不同长度木板的结果必有 k + 1 个，分别为 shorter * k + (longer - shorter) * i，其中 0 <= i <= k。
#
# 证明如下：
#
# 假如，假设取了 k - i 个 shorter 木板，则取了 i 个 longer 木板。
#
# 构成的总长度 f(i) 是：
#
#
# f(i) = shorter * (k - i) + longer * i
#      = shorter * k + (longer - shorter) * i
# 由于 longer - shorter > 0，所以 f(i) 是随着 i 的增长而单调递增的一元线性函数。
#
# 由一元线性函数的性质，我们知道函数 f(i) 不会有相同的取值。而 i 的取值是 0 <= i <= k，因此 f(i) 必有 k + 1 个不同的取值。
#
# 因此我们定义一个长度为 k + 1 的数组，把其中的每个位置分别设置为 shorter * (k - i) + longer * i 即可。
class Solution:
    def divingBoard(self, shorter, longer, k) :
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        res = [0] * (k + 1)
        for i in range(k + 1):
            res[i] = shorter * (k - i) + longer * i
        return res

# 面试题 16.11. 跳水板.py