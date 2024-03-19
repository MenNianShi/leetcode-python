# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        if len (digits) == 0:
            return []
        def backtrack(cur,index,digits):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return
            for c in phoneMap[digits[index]]:
                cur.append(c)
                backtrack(cur,index+1, digits)
                cur.pop()
        backtrack([],0,digits)
        return res






# 17. 电话号码的字母组合.py