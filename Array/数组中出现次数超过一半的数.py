# 加入数组中存在众数，那么众数一定大于数组的长度的一半。
# 思想就是：如果两个数不相等，就消去这两个数，最坏情况下，每次消去一个众数和一个非众数，那么如果存在众数，最后留下的数肯定是众数。
#
# 具体做法：
#
# 初始化：候选人cond = -1， 候选人的投票次数cnt = 0
# 遍历数组，如果cnt=0， 表示没有候选人，则选取当前数为候选人，++cnt
# 否则，如果cnt > 0, 表示有候选人，如果当前数=cond，则++cnt，否则--cnt
# 直到数组遍历完毕，最后检查cond是否为众数
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        cond = -1
        cnt = 0
        for num in numbers:
            if cnt==0:
                cond = num
                cnt+=1
            else:
                if num==cond:
                    cnt+=1
                else:
                    cnt-=1
        cnt = 0
        for num in numbers:
            if cond==num :
                cnt+=1

        if (cnt > len(numbers) // 2) :
            return cond
        else:
            return 0
# 数组中出现次数超过一半的数.py