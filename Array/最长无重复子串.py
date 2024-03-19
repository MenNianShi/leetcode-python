#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr ):
        # write code here
        n = len(arr)
        if n==0:
            return 0
        num_dict = {}
        left = 0
        right = 1
        num_dict[arr[0]] = 0
        max_length = 0
        while left<=right and right < n:
            if arr[right] in num_dict:
                while arr[left]!=arr[right]:
                    num_dict.pop(arr[left])
                    left+=1
                left+=1
            num_dict[arr[right]] = right
            max_length = max(max_length,len(num_dict))
            right+=1
        return max_length

class Solution:
    def maxLength(self, arr):
        # write code here
        n = len(arr)
        if n <= 1:
            return n
        left = 0
        right = 1
        max_len = 0
        cur = [arr[0]]
        while right < n:
            cur = arr[left:right]
            if arr[right] not in cur:
                cur.append(arr[right])
                right += 1

            else:
                cur.pop(0)
                left += 1
            max_len = max(max_len, len(cur))
        return max_len



# 最长无重复子串.py