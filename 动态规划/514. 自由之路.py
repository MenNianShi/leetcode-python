# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         import collections, functools
#         lookup = collections.defaultdict(list)
#         steps = collections.defaultdict(int)
#         # 把所有可以旋转的字符串找出来
#         for i in range(len(ring)):
#             tmp = ring[i:] + ring[:i]
#             # 加入以开头字母为键的数组中
#             lookup[ring[i]].append(tmp)
#             # 距离原始ring顺时针旋转需要几步
#             steps[tmp] = i
#
#         # 从一个字符串到另一字符串最少旋转的步数
#         def cal_steps(cur, nxt):
#             return min(tmp: = abs(steps[cur] - steps[nxt]), len(ring) - tmp)
#
#             @functools.lru_cache(None)
#             def dfs(cur, k):
#                 if k == len(key):
#                     return 0
#                 res = float("inf")
#                 for word in lookup[key[k]]:
#                     res = min(res, cal_steps(cur, word) + 1 + dfs(word, k + 1))
#                 return res
#
#             return dfs(ring, 0)

# 514. 自由之路.py