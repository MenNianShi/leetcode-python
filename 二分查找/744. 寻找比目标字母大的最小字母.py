class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        index = self.binsearch(letters,target)
        if index>=len(letters) or index<0:
            return letters[0]
        else:
            return letters[index]
    def binsearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<target:
                left= mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                left = left + 1
        return left
a  = Solution()
print(a.nextGreatestLetter(["c","f","j"],'a'))