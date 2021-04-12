# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]   打印杨辉三角形
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    l=[]
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1],[1,1]]
    if numRows >2:
        l= [[1],[1,1]]
    for i in range(2,numRows):
        temp = []
        for j in range(0,i+1):
            if j-1>=0 and j<len(l[i-1]) :
                temp.append(l[i-1][j-1]+l[i-1][j])
            if j-1<0 and j<len(l[i-1]) :
                temp.append(l[i-1][j])
        l.append(temp)
    return l
print(generate(5))
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ret = []
        for i in range(numRows):
            ret.append([1])
            for j in range(1,i+1):
                if j==i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i-1][j]+ret[i-1][j-1])
        return ret
class Solution(object):
    def generate(self,numRows):
        res = [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res