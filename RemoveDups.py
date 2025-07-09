'''
Constraints:
- Integer data values
- Singly linked list
'''


class Node:
    def __init__(self, data):
        self.val = data  # < node value
        self.next = None  # < next node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
            while curr is not None:
                print(curr.val)
                curr = curr.next

    '''
    Time : O(n)
    Space : O(n)
    1. Use hash table to mark visited nodes
    2. Iter through and perform deletion on already visited nodes
    '''

    def removeDups(self):
        # empty linked list
        if self.head is None:
            return

        curr = self.head  # < pointer to head
        table = {}  # < table to track nodes already seen
        while curr and curr.next:  # < need to check both current and next in case current gets moved out-of-bounds
            # visit node
            table[curr.val] = 1
            # next node already seen, skip it
            if curr.next.val in table:
                curr.next = curr.next.next
            # next node
            curr = curr.next

    '''
    Two-pointer deletion 
    1. Fast ptr searches ahead for curr node and deletes if found
    2. Reset fast ptr each for each new node 
    Time : O(n^2)
    Space : O(1)
    '''
    def removeDupsByPointers(self):
        # empty linked list or only one element
        if not self.head or not self.head.next:
            return

        # two pointers
        slow = fast = self.head

        while slow and slow.next:
            while fast and fast.next:
                if fast.next.val == slow.val:
                    fast.next = fast.next.next
                fast = fast.next
            slow = slow.next
            fast = slow


linkedList = LinkedList()

nodeA = Node(1)
nodeB = Node(1)
nodeC = Node(2)
nodeD = Node(2)
nodeE = Node(3)
nodeF = Node(2)

linkedList.append(nodeA)
linkedList.append(nodeB)
linkedList.append(nodeC)
linkedList.append(nodeD)
linkedList.append(nodeE)
linkedList.append(nodeF)

linkedList.print()
print()
linkedList.removeDups()
linkedList.print()
print()

linkedListTwo = LinkedList()

nodeA = Node(1)
nodeB = Node(1)
nodeC = Node(2)
nodeD = Node(2)
nodeE = Node(3)
nodeF = Node(2)

linkedListTwo.append(nodeA)
linkedListTwo.append(nodeB)
linkedListTwo.append(nodeC)
linkedListTwo.append(nodeD)
linkedListTwo.append(nodeE)
linkedListTwo.append(nodeF)

linkedListTwo.print()
print()
linkedListTwo.removeDupsByPointers()
linkedListTwo.print()
