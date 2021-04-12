class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops: return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m * n
        min0 = ops[0][0]
        min1 = ops[0][1]

        for p in ops:
            if p[1] < min1:
                min1 = p[1]
            if p[0] < min0:
                min0 = p[0]

        return min0 * min1
