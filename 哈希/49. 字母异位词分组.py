# 49 字母异位词分组
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        str_dict = {}
        for string in strs:
            s_hash = ''.join(sorted(list(string)))
            if s_hash not in str_dict:
                str_dict[s_hash] = [string]
            else:
                str_dict[s_hash].append(string)
        for k, v in str_dict.items():
            res.append(v)
        return res
