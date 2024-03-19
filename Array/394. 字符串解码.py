# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
# 示例:
#
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

# 构建辅助栈 stack， 遍历字符串 s 中每个字符 c；
# 当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算；
# 当 c 为字母时，在 res 尾部添加 c；
# 当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 00：
# 记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
# 记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
# 进入到新 [ 后，res 和 multi 重新记录。
# 当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
# last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
# cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。
# 返回字符串 res。

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res
#递归
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)


# 394. 字符串解码.py