# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
#
# 注意:
#
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
# 示例 1 :
#
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
#贪心+ 单调栈如果 后一个数 大于 前一个数， 那么就应该删除前一个数，
class Solution:
    def removeKdigits(self, num, k) :
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"

# 402. 移掉K位数字.py