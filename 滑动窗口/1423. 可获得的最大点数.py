class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        window_size = len(cardPoints) - k
        all_sum = sum(cardPoints)
        s = sum(cardPoints[:window_size])
        min_sum = s
        for i in range(window_size, len(cardPoints)):
            s += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, s)
        return all_sum - min_sum
        # 递归超时
        # if k == 0:
        #     return 0
        # left_res = cardPoints[0] + self.maxScore(cardPoints[1:], k-1)
        # right_res = cardPoints[-1] + self.maxScore(cardPoints[:-1], k-1)
        # return max(left_res, right_res)





