def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    allUpper = True
    allLower = True
    for i in word:
        if ord(i)>90 or ord(i)<65:
            allUpper = False
    if allUpper == True:
        return True
    for i in word:
        if ord(i)>122 or ord(i)<97:
            allLower = False
    if allLower == True:
        return True
    flag = True
    if ord(word[0])>=65 and ord(word[0])<=90:
        for i in word[1:]:
            if ord(i)> 122 or ord(i) < 97:
                flag = False
        if flag ==True:
            return True
    return False
print(detectCapitalUse('fffffffffffffF'))
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return  word.isupper() or word.istitle() or word.islower()
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        else:
            c = word[0]
            e = word[1:]
            if e.islower() and c.isupper():
                return True
        return False