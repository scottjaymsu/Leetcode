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

linkedList = LinkedList([3,5,8,5,10,2,1])
linkedList.print()

def Partition(linkedList, partition):
    # edge case : null linked list or null partition
    if linkedList is None or partition is None:
        return None

    # initialize linked lists for both sides of partition
    left, right = LinkedList(), LinkedList()
    copyLeft = left

    # iterate through the linked list
    while linkedList.head:
        # append based on partition
        value = linkedList.head.val
        if value < partition:
            left.val = value  # < shallow copy node value
            left.next = LinkedList()  # < copies next node
            left = left.next  # < shift over left to new node
        else:
            right.val = value
            right.next = LinkedList()
            right = right.next

    # append the head of the right side to the tail of the next
    left.val = right.head.val
    left.next = right.head.next

    left.print()
    return copyLeft

print(Partition(linkedList,partition=5))