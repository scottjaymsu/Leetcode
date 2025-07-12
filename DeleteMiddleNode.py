class Node:
    def __init__(self, data=None):
        self.val = data  # < node value
        self.next = None  # < next node


class LinkedList:
    def __init__(self, list=None):
        self.head = None
        self.tail = None
        if list:
            for num in list:
                node = Node(num)
                self.append(node)
    def append(self, node):
        # empty list
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next  # < iterate until end of list is found
            curr.next, self.tail = node, node

    def print(self):
        # empty list
        if self.head is None:
            print()
        else:
            curr = self.head
            values = []
            while curr is not None:
                values.append(curr.val)
                curr = curr.next
            print(values)

    # return node at index (zero-based), if doesn't exist return null node
    def giveNodeAtIndex(self, index):
        i = 0
        copy = self.head
        # [1,2,3,4] -> giveNodeAtIndex(2) = Node(3)
        while copy and i < index:
            copy = copy.next
            i += 1
        return copy if copy else Node()

linkedList = LinkedList(['a', 'b', 'c', 'd', 'e', 'f'])
linkedList.print()
print(linkedList.giveNodeAtIndex(2).val)

# Constraint : only middle (no first/last node)
'''
Time : O(1)
Space : O(1)
'''
def DeleteMiddleNode(node):
    # edge case : null input or tail given
    if not node or not node.next:
        return

    nextNode = node.next #< copy of next node (right after middle)
    node.val = nextNode.val #< copies data from next to middle
    node.next = nextNode.next #< basically keeps the first (middle) node and skips over the old copy
    return

DeleteMiddleNode(linkedList.giveNodeAtIndex(2))
linkedList.print()