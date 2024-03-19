# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#插入排序
#将每个人按照身高从大到小进行排序，k 值从小到大排序 ，后面进行插入排序即可
class Solution:
    def reconstructQueue(self, people) :
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans
a = Solution()
print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
# 406. 根据身高重建队列.py