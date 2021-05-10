# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 说明：
#
# 无空格字符构成一个 单词 。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#  
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-words-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return s
        s = self.trim_spaces(s)

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

    def trim_spaces(self, s):
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

class Solution:
    def trim_spaces(self, s):
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l):
        n = len(l)
        start = end = 0

        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1

    def reverseWords(self, s):
        l = self.trim_spaces(s)

        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)

        # 翻转每个单词
        self.reverse_each_word(l)

        return ''.join(l)

