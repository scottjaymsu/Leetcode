class Node:
    def __init__(self, data):
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

linkedList = LinkedList([1,2,3,4,5,6])
linkedList.print()

'''
** Implement an algorithm to find the kth to last element of a singly linked list **

Example:
1 -> 2 -> 3 -> 4 -> 5 -> 6
KthElement(LinkedList, 3) = Node 3

Brute-force
1. fast and slow pointer, where fast pointer is k elements ahead
2. iterate until fast.next == NULL
3. return slow
Edge cases : 
- LinkedList smaller than k elements
- Empty linked list / NULL input
- Negative k value
- k = 0 (last element)
Time : O(n), Space : O(1)

'''

def KthElement(linkedList, k):
    # edge case : empty linked list
    if linkedList is None or linkedList.head is None or k < 0:
        return None

    # two-pointer algorithm
    slow, fast = None, linkedList.head
    # iterate fast pointer without the slow pointer moving
    # until the faster pointer is k elements ahead
    count = 0

    # boundaries for fast pointer
    while fast:
        # initialize slow pointer to head when fast pointer is k-elements ahead
        if count == k :
            slow = linkedList.head
        elif count >= k:
            slow = slow.next
        count += 1
        fast = fast.next


    return slow.val if slow else None #< edge case : would return None if there are not at least k elements

print(KthElement(linkedList, k=3)) #< return 3
print(KthElement(None, k=3)) #< edge case : NULL input
print(KthElement(LinkedList(), k=3)) #< edge case : empty LinkedList
print(KthElement(linkedList, k=8)) #edge case : k > n
print(KthElement(linkedList, k=-1)) #edge case : k < 0
print(KthElement(linkedList, k=0)) #edge case : k = 0 (last element)

'''
# Other methods
1. If the linkedList size is passed in, then could return Node at n - k - 1
2. Recursively : Find Node(n-1), then recurse back k times
'''
