def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    l = []
    a =set(nums1)
    b = set(nums2)
    for i in b:
        if i in a:
            l.append(i)
    return l


print(intersection([1, 2, 2, 1],[2,2]))
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))