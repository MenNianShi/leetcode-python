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

class Solution:
    def letterCombinations(self, digits) :
        if not digits:
            return list()

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
        combinations = []
        combination = []
        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                for  letter in phoneMap[digits[index]]:
                    combination.append(letter)
                    backtrack(index+1)
                    combination.pop()
        backtrack(0)
        return  combinations




# 17. 电话号码的字母组合.py