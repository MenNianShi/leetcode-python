# You are given a string representing an attendance record for a student. The record only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False
def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    a =set('PLA')
    for i in s:
        if i not in a:
            return False
    if s.count('A')>1:
        return False
    for i in range(0,len(s)):
        if s[i]=='L' and (i+2)<len(s):
            if s[i+1]=='L' and s[i+2]=='L':
                return False
    return True

print(checkRecord('ALL'))