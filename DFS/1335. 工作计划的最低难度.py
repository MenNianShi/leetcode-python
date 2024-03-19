from functools import lru_cache
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        @lru_cache(None)
        def dfs(left:int,day:int)->int:
            if day == 1:
                return max(jobDifficulty[left:])
            base = 0
            result = sum(jobDifficulty[left:])
            for i in range(left,len(jobDifficulty)-day+1):
                base = max(base,jobDifficulty[i])
                result = min(result,base+dfs(i+1,day-1))
            return result
        if d > len(jobDifficulty):
            return -1
        return dfs(0,d)
# 1335. 工作计划的最低难度.py