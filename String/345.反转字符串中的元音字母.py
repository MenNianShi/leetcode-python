# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".aeiou
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    tmp=''
    s = list(s)
    for i in range(0,len(s)):
        if s[i] in set(['a','e','i','o','u']):
            tmp = tmp+s[i]
            s[i] = ' '
    tmp = tmp[::-1]
    for i in range(0,len(s)):
        if s[i] ==' ':
            s[i] = tmp[0]
            tmp = tmp[1:]
    res = ''
    for i in range(0,len(s)):
        res = res + s[i]
    return res
print(reverseVowels('leetcode'))
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        vowels = []
        for i in xrange(len(res)):
            if res[i] in ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']:
                vowels.append((i, res[i]))
        for j in xrange(len(vowels)/2):
            res[vowels[j][0]] = vowels[len(vowels)-j-1][1]
            res[vowels[len(vowels)-j-1][0]] = vowels[j][1]
        return ''.join(res)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a': True, 'o': True, 'e': True, 'i': True, 'u': True, 'A': True, 'O': True, 'E': True, 'I': True,
                  'U': True}
        res = list(s)
        pos = []
        for i in xrange(len(res)):
            if res[i] in vowels:
                pos.append((i, res[i]))
        for j in xrange(len(pos) / 2):
            res[pos[j][0]] = pos[len(pos) - j - 1][1]
            res[pos[len(pos) - j - 1][0]] = pos[j][1]
        return ''.join(res)
# 345.反转字符串中的元音字母.py