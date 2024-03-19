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


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        memo = dict()

        def dp(K, N):
            # base case
            if K == 1: return N
            if N == 0: return 0
            # 避免重复计算
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 穷举所有可能的选择
            for i in range(1, N + 1):
                res = min(res,
                          max(
                              dp(K, N - i),
                              dp(K - 1, i - 1)
                          ) + 1
                          )
            # 记入备忘录
            memo[(K, N)] = res
            return res

        return dp(K, N)


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        memo = dict()

        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)  # 碎
                not_broken = dp(K, N - mid)  # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)

            memo[(K, N)] = res
            return res

        return dp(K, N)
# 887. 鸡蛋掉落.py