# 拉链法是说，我们定义了一个比较小的数组，然后使用 hash 方法来把求出 key 应该出现在数组中的位置；但是由于不同的 key 在求完 hash 之后，可能会存在碰撞冲突，所以数组并不直接保存元素，而是每个位置都指向了一条链表（或数组）用于存储元素。
#
# 我们可以看出在查找一个 key 的时候需要两个步骤：① 求hash到数组中的位置；② 在链表中遍历找key。
#
# 优点：我们可以把数组大小设计比较合理，从而节省空间；不用预知 key 的范围；方便扩容。
# 缺点：需要多次访问内存，性能上比超大数组的 HashSet 差；需要设计合理的 hash 方法实现均匀散列；如果链表比较长，则退化成 O(N)O(N) 的查找；实现比较复杂；
# 在下面的具体实现中，我把拉链设计成了基于「数组」的实现（也可以基于链表）。此时「拉链数组」有两种设计方法：①定长拉链数组；②不定长拉链数组。
# 不定长的拉链数组是说拉链会根据分桶中的 key 动态增长，更类似于真正的链表。
#
# 分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
#
# 优点：节省内存，不用预知数据范围；
# 缺点：在链表中查找元素需要遍历。
#
class MyHashSet:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key):
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key):
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key):
        hashkey = self.hash(key)
        return key in self.table[hashkey]

# 705. 设计哈希集合.py