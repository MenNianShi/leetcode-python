from  collections import  Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return Counter(word1).keys() == Counter(word2).keys() and sorted(Counter(word1).values()) == sorted(Counter(word2).values())

# 1657. 确定两个字符串是否接近.py