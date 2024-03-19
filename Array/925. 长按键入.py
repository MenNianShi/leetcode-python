# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
#
#  
#
# 示例 1：
#
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex' 中的 'a' 和 'e' 被长按。
# 示例 2：
#
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
#
class Solution:
    def isLongPressedName(self, name, typed):
        i,j = 0,0
        n,m = len(name),len(typed)
        # 开始第一个进行判断
        if name[i]!=typed[j]:
            return False
        #进入循环，如果name[i]==typed[j]，那么指针同时指向第二个值，如果不等则判断typed的值是否和
        #name前一个值相等，如果相等，则typed指针向后移，如果不等则False
        while i<n and j<m:
            if name[i]==typed[j]:
                i += 1
                j += 1
            else:
                if typed[j] == name[i-1]:
                    j += 1
                else:
                    return False
        # 退出循环如果name,typed刚好结束判断
        if i == n and j == m:
            return True
        # 退出循环，如果typed刚好结束而name没结束，说明name后还有字符
        if i<n:
            return False
        # 退出循环，如果name刚好结束而typed没结束，判断typed后面的字符是否和name最后一个字符相等
        if j<m:
            if ''.join(set(typed[j:]))==typed[j]:
                return True
            return False

# 925. 长按键入.py