
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):

    random_dict = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None :
            return None
        if head not in self.random_dict:
            headNew = Node(head.val)
            self.random_dict[head] = headNew
            headNew.next = self.copyRandomList(head.next)
            headNew.random = self.copyRandomList(head.random)
        return self.random_dict[head]

