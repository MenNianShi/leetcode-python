# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_dict={}
    t_dict={}
    for i in s :
        if i not in s_dict:
            s_dict[i] =1
        else:
            s_dict[i]+=1
    for i in t :
        if i not in t_dict:
            t_dict[i] =1
        else:
            t_dict[i]+=1
    if s_dict == t_dict:
        return True
    else:
        return False
print(isAnagram("anagram", "nagaram"))


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        elif s == '' and t == '':
            return True
        elif s == t:
            return True
        else:
            ans = 1
            sSet = set(list(s))
            for n in sSet:
                if n in t:
                    if s.count(n) == t.count(n):
                        continue
                    else:
                        ans = 0
                        break
                else:
                    ans = 0
                    break
            return bool(ans)

# 242.有效的字母异位词.py