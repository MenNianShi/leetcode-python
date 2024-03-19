class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, k, res = [],0,''
        for c in s:
            if '0' <= c <='9':
                k = k *10 + int(c)
            elif c == '[':
                stack.append([k,res])
                res ,k = "",0
            elif c == ']':
                cur_k , last_res = stack.pop(-1)
                res = last_res + cur_k * res
            else:
                res = res + c
        return res

# 394. 字符串解码