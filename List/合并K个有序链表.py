#coding=utf-8
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def getMinNode(lists):
    minNode = ListNode(float('inf'))
    index = -1
    for i in range(len(lists)):
        if lists[i] and lists[i].val < minNode.val:
            minNode = lists[i]
            index = i
    if minNode.val != float('inf'):
        return minNode, index
    else:
        return None, -1

def mergeKLists(lists):

    dummy = ListNode(0)
    p = dummy
    i = 0
    while i<len(lists):
        if lists[i]==None:
            lists.pop(i)
        else:
            i+=1
    while len(lists) > 0:
        node, index = getMinNode(lists)
        if node:
            p.next = node
            lists[index] = lists[index].next
            if lists[index] == None:
                lists = lists[:index] + lists[index + 1:]

            p = p.next
    return dummy.next