class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_dict = collections.Counter(p)
        left ,right = 0,0
        valid = 0
        wind_dict = {}
        res = []
        while right < len(s):
            c = s[right]
            right +=1
            #     进行窗口内数据的一系列更新
            if c in p_dict:
                if c not in wind_dict :
                    wind_dict[c] = 1
                else :
                    wind_dict[c] +=1
                if wind_dict[c] == p_dict[c]:
                    valid+=1

            # 判断左侧窗口是否要收缩
            while (right- left) >= len(p):
                if valid == len(p_dict):
                    res.append(left)
                d = s[left]
                left +=1
                # 进行窗口内数据的一系列更新
                if d in p_dict:
                    if wind_dict[d] == p_dict[d]:
                        valid-=1
                    wind_dict[d]-=1
        return res