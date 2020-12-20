class Node(object):
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class DoubleList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    # 新增node 加到 tail
    def addLast(self,node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
    #删除node
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    # pop 首个node，用于 跳出最久未使用node
    def popFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first
    def getSize(self):
        return self.size
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache_map = {}
        self.cache = DoubleList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache_map:
            return -1
        self.makeRecently(key)
        node = self.cache_map[key]
        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache_map:
            self.deleteNode(key)
            self.addRecently(key,value)
            return
        if self.cache.getSize() == self.capacity:
            self.removeLeastRecently()
        self.addRecently(key,value)
    #将某个key 调为最近使用
    def makeRecently(self,key):
        node = self.cache_map[key]
        self.cache.remove(node)
        self.cache.addLast(node)
    # 新增node 并标记为最近使用
    def addRecently(self,key,value):
        node = Node(key,value)
        self.cache.addLast(node)
        self.cache_map[key] = node
    #删除key
    def deleteNode(self,key):
        node = self.cache_map[key]
        self.cache_map.pop(key)
        self.cache.remove(node)
    # 删除最久未使用 node
    def removeLeastRecently(self):
        node = self.cache.popFirst()
        self.cache_map.pop(node.key)
lRUCache =  LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
print(1)