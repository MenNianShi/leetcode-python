
def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    n1 = list(findNums)
    n2 = list(nums)
    result = []
    count = 0

    for i in n1:
        index = 0
        for j in n2:
            if (i==j)and(index!=len(n2)-1):

                for x in n2[index+1:]:
                    if x>i:
                        count=1
                        result.append(x)
                        break
            index = index+1
        if count==0:
            result.append(-1)
        count = 0

    return result
print(nextGreaterElement([4,1,2],[1,3,4,2]))


def nextGreaterElement(self, findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    greater, stack = {}, []
    for n in nums:
        while stack and n > stack[-1]:
            greater[stack.pop()] = n
        stack.append(n)
    return [greater[n] if n in greater else -1 for n in findNums]