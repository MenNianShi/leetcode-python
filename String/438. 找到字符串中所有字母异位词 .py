class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n, step = len(s), len(p)
        sp = sorted(p)
        pset = set(p)

        result = []
        idx = 0
        # idx to idx+step (idx+step <= n)
        while idx < n - step + 1:
            if s[idx] in pset:
                if sp == sorted(s[idx:idx + step]):
                    result.append(idx)
                    while idx < (len(s) - step):
                        # extend to last one so idx cannot be len(s) - step
                        if s[idx] == s[idx + step]:
                            idx += 1
                            result.append(idx)
                        else:
                            if s[idx + step] not in pset:
                                idx += step
                            break
            idx += 1
        return result
a = Solution()
print(a.findAnagrams("cbaebabacd" ,"abc"))
from collections import Counter

class Solution(object):
     def findAnagrams(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: List[int]
         """
         size = len(p)
         n    = len(s)
         pCounter = Counter(p)
         sCounter = Counter(s[:size-1])

         ans = []

         for i in range(size-1,n):
             sCounter[s[i]] += 1
             if sCounter == pCounter:
                 ans.append(i-size+1)
             if sCounter[s[i-size+1]] == 1:
                 del sCounter[s[i-size+1]]
             else:
                 sCounter[s[i-size+1]] -= 1
         return ans


# 438. 找到字符串中所有字母异位词 .py