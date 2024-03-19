# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
#
# 示例1:
#
#  输入：nums = [0, 2, 3, 4, 5]
#  输出：0
#  说明: 0下标的元素为0

#这道题应该是无法使用真正的二分法的，因为在这一段数组中，**元素大小不保证严格单调，所以我们无法根据中点值排除掉数组的某一半搜索区间**。所以最快的方法仍然是**O(n)**，我们最多想办法将时间复杂度稍微降低一点。详细见代码，我们可以根据当前值的大小，试着**跳跃性排除**数组中的一小段。

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                return i
            if nums[i] > i:  # 此时我们可以排除索引i到nums[i-1]这一整段
                i = nums[i]  # 由于数组可以保持平稳，所以nums[i]这一元素不可排除
            else:
                i += 1

        return -1


class Solution(object):
    res =-1
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.binsearch(nums,0,len(nums)-1)
        return self.res
    def binsearch(self,nums,left,right):
        if left<=right:
            mid = left + (right-left)//2

            if mid == nums[mid]:
                self.res = mid
                self.binsearch(nums,left,mid-1)
            else:
                self.binsearch(nums,left,mid-1)
                if self.res==-1 :
                    self.binsearch(nums,mid+1,right)
        else:
            return

a = Solution()
print(a.findMagicIndex([12296169, 14481887, 19365401, 71948694, 101256536, 137449705, 147615033, 169095970, 182939974, 183054331, 191033174, 200069688, 210281043, 211549396, 227193353, 252408327, 263757832, 268669870, 271916258, 293898012, 322628245, 329246885, 348479255, 405807814, 431800160, 449369511, 477566467, 481431749, 481880069, 487953610, 509211052, 520721303, 527744664, 550058864, 571603718, 571617555, 579098239, 582152388, 645340207, 681566032, 685774515, 706348591, 708774328, 717815831, 721421995, 724666698, 745560058, 746289154, 769651867, 781893631, 789714924, 807615645, 882508445, 884260053, 916797901, 920985226, 924045345, 932899253, 950715182, 987825772, 1015158842, 1016121780, 1065377233, 1072449577]))
# 08.03. 魔术索引.py