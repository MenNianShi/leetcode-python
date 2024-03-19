class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, begin):

        if target == 0:
            self.resList.append(sublist[:])

        for i in range(begin,len(candidates)):
            if candidates[i] > target:  #大于 肯定加不进list
                return
            if i > begin and candidates[i]==candidates[i-1]: # 由于已排过序， 所以 至少应和 last 相同。
                continue
            sublist.append(candidates[i])
            self.dfs(candidates,sublist,target - candidates[i], i+1)
            sublist.pop()
a = Solution()
print(a.combinationSum2([10,1,2,7,6,1,5],8))
# 40. 组合总和 II.py