class Solution(object):
    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
        max_level_up = max(vat)
        n = len(bucket)
        if max_level_up == 0:
            return 0 
        res = float('inf')
        for k in range(1,max_level_up+1):
            t = 0
            for i in range(n):
                t += max(0,(vat[i] + k - 1) // k - bucket[i])
            res = min(res,  t + k)
        return int(res) 