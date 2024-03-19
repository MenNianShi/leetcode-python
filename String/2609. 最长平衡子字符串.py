# 给你一个仅由0和1组成的二进制字符串s 。
# 如果子字符串中所有的0都在1
# 之前且其中0的数量等于1的数量，则认为s的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。
# 返回s中最长的平衡子字符串长度。子字符串是字符串中的一个连续字符序列。
# 示例
# 1：
# 输入：s = "01000111"
# 输出：6
# 解释：最长的平衡子字符串是
# "000111" ，长度 6 。


class Solution:
    def findTheLongestBalancedSubstring(self, s) :
        res = 0
        n = len(s)
        count = [0, 0] # index = 0 记录遇到的连续0个数，index =1 记录遇到的连续1个数
        for i in range(n):
            if s[i] == '1':
                count[1] += 1
                res = max(res, 2 * min(count))
            elif i == 0 or s[i-1] == '1': # 遇到的 第一个 '0'
                count[0] = 1
                count[1] = 0
            else:  # 遇到的 非第一个 '0'
                count[0] += 1
        return res

class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_index = s.find("01")
        max_res = 0
        while s_index != -1:
            res = 2
            i = 1
            while (s_index-i >= 0) and (s_index+i+1 < len(s)):
                if s[s_index-i] == "0" and s[s_index+i+1] == "1":
                    res += 2
                    i+=1
                else:
                    max_res = max(max_res, res)
                    break
            if (s_index + 2) <= len(s):
                tmp = s[s_index+2:]
                tmp_index = tmp.find("01")
                if tmp_index == -1:
                    max_res = max(max_res, res)
                    break
                else:
                     s_index = tmp_index + len(s[:s_index+2])
            else :
                max_res = max(max_res, res)
                break
            max_res = max(max_res,res)
        return max_res
# 2609. 最长平衡子字符串.py