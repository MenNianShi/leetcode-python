class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s) == 0: return s
        s = list(s)
        strs = self.reverse(s, 0, len(s) - 1)
        left = 0
        right = 0
        while left < len(strs):
            if strs[left] == ' ':
                left += 1
                right += 1
            elif (right == len(strs) or strs[right] == ' '):
                strs = self.reverse(strs, left, right - 1)
                right += 1
                left = right
            else:
                right += 1
        return ''.join(strs)

    def reverse(self, strs, left, right):
        while left < right:
            strs[left], strs[right] = strs[right], strs[left]
            left += 1
            right -= 1
        return strs
# 反转单词序列.py