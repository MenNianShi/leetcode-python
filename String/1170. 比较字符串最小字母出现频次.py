# 首先将两个字符串的数组分别转化为对应的出现次数的数组 接下来对words对应的数组进行排序 最后对于每一个query进行二分查找
# 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
#
# 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
#
# 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足 f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
#
# 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        w,q=[],[]
        for word in words:
            cur=0
            minc='z'
            for c in word:
                if c ==minc:
                    cur+=1
                elif c<minc:
                    cur=1
                    minc=c
            w.append(cur)
        for query in queries:
            cur=0
            minc='z'
            for c in query:
                if c ==minc:
                    cur+=1
                elif c<minc:
                    cur=1
                    minc=c
            q.append(cur)
        w.sort()
        ans = []
        for query in q:
            l,r=0,len(w)-1
            while l<=r:
                mid=l+(r-l)//2
                if w[mid]<=query:
                    l=mid+1
                else:
                    r=mid-1
            ans.append(len(w)-l)
        return ans
