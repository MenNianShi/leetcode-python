# 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。
#
# 从 n 个元素中选择一个子集 s :
#
# 子集 s 的大小 小于或等于 numWanted 。
# s 中 最多 有相同标签的 useLimit 项。
# 一个子集的 分数 是该子集的值之和。
#
# 返回子集 s 的最大 分数 。
# 我们首先将元素按照 values 的值进行降序排序。待排序完成后，我们依次遍历每个元素并判断是否选择。我们可以使用一个变量 choose 记录已经选择的元素个数，以及一个哈希表记录每一种标签已经选择的元素个数（键表示标签，值表示该标签已经选择的元素个数）：
#
# 如果 choose=numWanted，我们可以直接退出遍历；
#
# 如果当前元素的标签在哈希表中对应的值等于 useLimit，我们忽略这个元素，否则我们选择这个元素，并更新 choose、哈希表以及答案。
#
# 细节
#
# 由于题目中的 values 和 labels 是分成两个数组给出的，直接排序会比较困难。我们可以额外开辟一个同样长度为 nnn 的数组，存储下标，并直接在该数组上进行排序即可。


class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        n = len(values)
        idx = list(range(n))
        idx.sort(key = lambda i : -values[i])

        ans = choose = 0
        cnt = Counter()
        for i in range(n):
            label = labels[idx[i]]
            if cnt[label] == useLimit:
                continue
            choose += 1
            ans += values[idx[i]]
            cnt[label] += 1
            if choose == numWanted:
                break
        return ans
# 1090. 受标签影响的最大值.py