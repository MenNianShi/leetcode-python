class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        rownum=rowIndex+1
        currow=[1]
        if rownum==1:
            return currow
        if rownum>0:
            currow=[1]
            for index in range(rownum):
                prerow=currow
                currow=[1]
                for j in range(index-1):
                    currow.append(prerow[j]+prerow[j+1])
                currow.append(1)
        return currow
# 119.杨辉三角 II .py