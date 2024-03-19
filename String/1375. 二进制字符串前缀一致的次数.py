# 在第 i 次翻转之后，我们希望 [1,i] 内的所有位都是 1，这等价于「前 i次翻转中下标的最大值等于 i。
#
# 因此，我们对数组 flip 进行遍历，同时记录翻转下标的最大值。当遍历到位置 i 时，如果最大值恰好等于 i，那么答案加 1。
#
# 需要注意数组的下标是从 0 开始的，因此在实际的代码编写中，判断的值为 i+1。

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = right = 0
        for i, flip in enumerate(flips):
            right = max(right, flips[i])
            if right == i + 1:
                ans += 1
        return ans

class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        def check(bin_str, index):
            check_str = '1' * index
            if bin_str[:index] == check_str:
                return True
            else:
                return False
        n = max(flips)
        bin_str = '0' * (n)
        res = 0
        for i in range(len(flips)):
            bin_str = bin_str[:flips[i]-1] + '1' + bin_str[flips[i]:]
            if check(bin_str, i+1):
                res+=1
        return res

a = Solution()
print(a.numTimesAllBlue([3,2,4,1,5]))
# 1375. 二进制字符串前缀一致的次数.py