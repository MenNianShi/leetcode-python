# # Given an array of characters, compress it in-place.
# #
# # The length after compression must always be smaller than or equal to the original array.
# #
# # Every element of the array should be a character (not int) of length 1.
# #
# # After you are done modifying the input array in-place, return the new length of the array.
# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
#
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        put = 0
        move = 0
        while move < len(chars):
            char = chars[move]
            count = 1
            move += 1
            while move < len(chars) and chars[move] == char:
                move += 1
                count += 1
            if count == 1:
                chars[put] = char
                put += 1
            else:
                chars[put] = char
                put += 1
                count = str(count)
                for c in count:
                    chars[put] = c
                    put += 1
        return put
def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    dict1={}
    l = []
    for i in range(0,len(chars)):
        if chars[i] not in dict1:
            dict1[chars[i]] = 1
        else:
            dict1[chars[i]] += 1
    print(dict1)
    for k,v in dict1.items():
        if v==1 :
            l.append(k)
        if v>1:
            l.append(k)
            for i in list(str(v)):
                l.append(i)

    return l

chars = ["a","a","b","b","c","c","c"]
print(compress(chars))
