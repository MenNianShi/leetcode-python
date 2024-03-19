# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
#
# 你可以按任意顺序返回答案。
#
#  
#
# 示例 1：
#
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
# 示例 2：
#
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
#  
#
import  collections
class Solution:
    def commonChars(self, A) :
        ans=collections.Counter(A[0])
        for i in A:
            ans=ans&collections.Counter(i)
        return list(ans.elements())


class Solution:
    def commonChars(self, A) :
        minfreq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord("a")] += 1
            for i in range(26):
                minfreq[i] = min(minfreq[i], freq[i])

        ans = list()
        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minfreq[i])
        return ans




# 1002. 查找常用字符.py