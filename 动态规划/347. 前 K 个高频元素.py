# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#  
#
# 示例
# 1:
#
# 输入: nums = [1, 1, 1, 2, 2, 3], k = 2
# 输出: [1, 2]
# 示例
# 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]

import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def shift(i,k):#维护最小堆
            while True:
                t=2*i+1
                if t >= k :
                    return
                if t+1<k and hashlist[t][1]>hashlist[t+1][1]:
                    t=t+1
                if hashlist[t][1]<hashlist[i][1]:
                    hashlist[t],hashlist[i]=hashlist[i],hashlist[t]
                    i=t
                else:
                    return


        #建立哈希表
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        #print(hashmap)
        #将哈希表转为二维列表
        hashlist=[ [key,v] for key, v in hashmap.items() ]
        #print(hashlist)
        #建立K个元素的最小堆
        for i in range(k/2,-1,-1):
            shift(i,k)
        #剩余依次和堆顶比较
        for i in range(k,len(hashlist)):
            if hashlist[i][1]>=hashlist[0][1]:
                hashlist[0]=hashlist[i]
                shift(0,k)
        return [hashlist[i][0] for i in range(k)]
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = collections.Counter(nums)
        res = []
        for key,v in s.items():
            res.append([key,v])
        res.sort(key=lambda x:x[1],reverse=True)
        ans = []
        for num in res[:k]:
            ans.append(num[0])
        return  ans
a = Solution()
print(a.topKFrequent([1,1,1,2,2,3]
,2))
# 347. 前 K 个高频元素.py