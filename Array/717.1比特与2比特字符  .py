# We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.
#
# Example 1:
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
# Example 2:
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
# 明白题目意图，就会发现，题目的意思是要判断最后一个0元素是属于0还是输入10；
# 遍历数组，给定指针，若当前位为1则指针+2；若当前位为0，则指针+1；
# 判断最后指针是否与bits.length-1相等，相等则为真，否则为假；其中length=1的情况也包括进去了。
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        start = 0
        while start < len(bits)-1:
            if bits[start]==1: start+=2
            else: start+=1
        return start==len(bits)-1
# 717.1比特与2比特字符  .py