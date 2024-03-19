# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    length = 0
    s_dict={}
    for i in s:
        if i not in s_dict:
            s_dict[i] = 1
        else:
            s_dict[i] +=1
    print(s_dict)
    for i in s_dict:
        if s_dict[i]%2==0:
            length += s_dict[i]
        else:
            length+= (s_dict[i]//2)*2
    if length!=len(s):
        return length+1
    else:
        return length
print(longestPalindrome('aaaAaaaa'))
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        mark = set(s)
        for ch in mark:
            result += s.count(ch)//2*2
        if len(s) != result:
            result += 1
        return result

# 409.最长回文串.py