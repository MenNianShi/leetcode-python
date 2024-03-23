# 380. O(1) 时间插入、删除和获取随机元素
import random
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val) :
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]
        self.indices[self.nums[id]] = id
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        return random.choice(self.nums)

# 变长数组可以在 O(1) 的时间内完成获取随机元素操作，但是无法在 O(1) 的时间内判断元素是否存在，
# 哈希表可以在 O(1)的时间内完成插入和删除操作, 但是由于无法根据下标定位到特定元素，因此不能在 O(1)的时间内完成获取随机元素操作。
# 为了满足插入、删除和获取随机元素操作的时间复杂度都是 O(1)
# 需要将变长数组和哈希表结合，变长数组中存储元素，哈希表中存储每个元素在变长数组中的下标。
# 删除操作的重点在于将变长数组的最后一个元素移动到待删除元素的下标处，
# 然后删除变长数组的最后一个元素。该操作的时间复杂度是 O(1)
# 且可以保证在删除操作之后变长数组中的所有元素的下标都连续，方便插入操作和获取随机元素操作。
#

