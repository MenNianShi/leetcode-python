# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
#   [7],
#   [2,2,3]
# ]
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(candidates,target,cur_list,last):
            if target==sum(cur_list):
                res.append(cur_list[:]) #深浅拷贝的问题  不加冒号出错
                return
            for index in range(last, len(candidates)):
                cur_list.append(candidates[index])
                if sum(cur_list)>target:
                    cur_list.pop()
                    break
                dfs(candidates,target,cur_list,index)
                cur_list.pop()
        candidates.sort()
        dfs(candidates,target,[],0)
        return res
a = Solution()
print(a.combinationSum([2,3,6,7],7))


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates = sorted(candidates)
        self.dfs(candidates,[],target,0)
        return self.resList
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target< candidates[0]:  # 如果 没有比目标值更小的数了
            return
        for n in candidates:
            if n > target:  #大于 肯定加不进list
                return
            if n < last: # 由于已排过序， 所以 至少应和 last 相同。
                continue
            sublist.append(n)
            self.dfs(candidates,sublist,target - n, n)
            sublist.pop()