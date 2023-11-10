# n对情侣坐在连续排列的2n个座位上，想要牵到对方的手。人和座位由一个整数数组
# row表示，其中row[i]是坐在第i个座位上的人的ID。情侣们按顺序编号，第一对是(0, 1)，第二对是(2, 3)，以此类推，最后一对是(n - 2, 2n - 1)。
#
# 返回最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。
#
#
#
# 示例1:
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 只需要交换row[1]和row[2]的位置即可。
# 示例2:
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row)
        res = 0
        for i in range(0, N - 1, 2):
            if row[i] == row[i + 1] ^ 1:
                # 不用交换
                continue
            for j in range(i + 1, N):
                if row[i] == row[j] ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    break
            res += 1
        return res
