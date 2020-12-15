# 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
#
# 每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
#
# 你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
#
# 每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
#
# 你的目标是确切地知道 F 的值是多少。
#
# 无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
# https://github.com/MenNianShi/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E9%AB%98%E6%A5%BC%E6%89%94%E9%B8%A1%E8%9B%8B%E8%BF%9B%E9%98%B6.md
#  
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        m = 0

        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1
        return m