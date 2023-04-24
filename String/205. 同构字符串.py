# 给定两个字符串
# s
# 和
# t ，判断它们是否是同构的。
#
# 如果
# s
# 中的字符可以按某种映射关系替换得到
# t ，那么这两个字符串是同构的。
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
#
#
# 示例
# 1:
#
# 输入：s = "egg", t = "add"
# 输出：true

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_dict = {}
        map_dict2 = {}

        if len(s)!=len(t) :
            return False
        i = 0
        while i<len(s):
            if s[i] not in map_dict:
                map_dict[s[i]] = t[i]
            else:
                if t[i] != map_dict[s[i]]:
                    return False
            i+=1
        i = 0
        while i<len(s):
            if t[i] not in map_dict2:
                map_dict2[t[i]] = s[i]
            else:
                if s[i] != map_dict2[t[i]]:
                    return False
            i+=1
        return True