def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    x = set(ransomNote)
    y = set(magazine)
    if x <= y:
        magazine_dict = {}
        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i]=1
            else:
                magazine_dict[i]+=1
        print(magazine_dict)
        for j in ransomNote:
            if j in magazine_dict:
                magazine_dict[j]-=1
        print(magazine_dict)
        for i in magazine_dict:
            if magazine_dict[i]<0:
                return False
        return True
    else:
        return False
print(canConstruct('aa','aab'))


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False

        return True