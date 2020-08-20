# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
#
#  
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        if len(s) > 12:
            return []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, path):
        if not s and len(path) == 4:
            tmp = '.'.join(path)
            self.res.append(tmp)
            return
        for i in range(1, 4):
            if i > len(s):
                continue
            cur = int(s[:i])
            if str(cur) == s[:i] and cur <= 255:
                self.dfs(s[i:], path + [s[:i]])



