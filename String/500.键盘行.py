class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set('QWERTYUIOPqwertyuiop')
        b = set('ASDFGHJKLasdfghjkl')
        c = set('ZXCVBNMzxcvbnm')
        l = []
        for i in words:
            temp = set(i)
            if temp.issubset(a) or temp.issubset(b) or temp.issubset(c):
                l.append(i)

        return l
a = Solution()
print(a.findWords(["Hello","Alaska","Dad","Peace"]))