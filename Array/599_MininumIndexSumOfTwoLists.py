def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    l = []
    miniSum = len(list1)+len(list2)-2
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i]==list2[j]:
                tempSum = i+j
                if tempSum<miniSum:
                    miniSum  = tempSum
                    l=[]
                    l.append(list1[i])
                elif tempSum == miniSum:
                    l.append(list1[i])

    return l
print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"]))


def findRestaurant(self, list1, list2):
    dic = {}
    for i, s in enumerate(list1):
        dic[s] = i

    sol = []
    min_sum = len(list1) + len(list2)
    for i, s in enumerate(list2):
        if s in dic:
            this_sum = dic[s] + i
            if this_sum < min_sum:
                sol = [s]
                min_sum = this_sum
            elif this_sum == min_sum:
                sol.append(s)

    return sol
