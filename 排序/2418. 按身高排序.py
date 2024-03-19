# 给你一个字符串数组names ，和一个由互不相同的正整数组成的数组heights 。两个数组的长度均为n 。
#
# 对于每个下标i，names[i]和heights[i]
# 表示第i个人的名字和身高。
# 请按身高降序顺序返回对应的名字数组names 。
# 示例1：
# 输入：names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
# 输出：["Mary", "Emma", "John"]
# 解释：Mary
# 最高，接着是Emma 和John 。
# 排索引即可
class Solution:
    def sortPeople(self, names, heights):
        n = len(names)
        indices = list(range(n))
        indices.sort(key=lambda x: heights[x], reverse=True)
        res = []
        for i in indices:
            res.append(names[i])
        return res


# 2418. 按身高排序.py