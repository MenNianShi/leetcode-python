# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
#
# 在结果列表中，选择字典序最小的名字作为真实名字。
#
# 示例：
#
# 输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"]
class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        name_dict = {}
        for synonym in synonyms:
            real_name = synonym.strip('(').strip(')').split(',')[0]
            fake_name = synonym.strip('(').strip(')').split(',')[1]
            if fake_name not in name_dict:
                name_dict[fake_name] = real_name
        name_res={}
        for name in names:
            n = name.split('(')[1].split(')')[0]
            f = name.split('(')[0]
            if f in name_dict:
                real_name = name_dict[f]
                if real_name not in name_res:
                    name_res[real_name] = int(n)
                else:
                    name_res[real_name]+=  int(n)
            else:
                if f not in name_res:
                    name_res[f] =  int(n)
                else:
                    name_res[f]+=  int(n)
        res = []
        for k,v in name_res.items():
            s = k+'('+str(v) + ')'
            res.append(s)
        res.sort()
        return res
a = Solution()
names  = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"]
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
print(a.trulyMostPopular(names,synonyms))
# 面试题 17.07. 婴儿名字.py