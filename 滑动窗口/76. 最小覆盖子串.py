# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
import  collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need_map = collections.defaultdict(int)
        min_len = float('inf')
        left = 0
        right ,count= 0,0
        res =""
        for c in t:
            need_map[c] += 1
        scount  = {}
        while right<len(s):
            c = s[right]
            scount[c]+=1
            if c in need_map and scount[c]<= need_map[c]:
                count+=1
            while left<=right and count==len(t):
                if min_len> right-left+1:
                    min_len = right-left+1
                    res = s[left:left+min_len]
                l = s[left]
                scount[l]-=1
                if l in need_map and scount[l]<need_map[l]:#此处不能相等，因为scount已经-过了
                    count-=1
                left += 1
            right+=1
        return  res





class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need_map = collections.defaultdict(int)

        left = 0
        right = 0
        res =""
        for c in t:
            need_map[c] += 1
        while right<=len(s):
            temp = s[left:right]
            if self.check(temp,need_map):
                if res =="":
                    res = temp
                else:
                    if len(temp)<len(res):
                        res = temp
                left+=1
            else:
                right+=1
        return res
    def check(self,temp,need_map):
        res_map = collections.defaultdict(int)
        for c in temp:
            res_map[c] += 1
        for k,v in need_map.items():
            if k in res_map:
                if res_map[k]>=v:
                    continue
                else:
                    return False
            else:
                return False
        return True
a =Solution()
print(a.minWindow("ADOBECODEBANC","ABC"))

# 76. 最小覆盖子串.py