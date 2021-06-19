# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
from typing import List


class Item:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = Item(0)
        self.tail = Item(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def getNode(self, index: int) -> Item:
        if index < self.size / 2:
            # start from start
            node = self.head
            for _ in range(index + 1):
                node = node.next
        else:
            # start from end
            node = self.tail
            for _ in range(self.size - index):
                node = node.prev
        return node

    def addNode(self, node: Item, val: int)-> None:
        item = Item(val)
        item.prev = node
        item.next = node.next
        node.next.prev = item
        node.next = item
        self.size += 1

    def removeNode(self, node: Item) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        return self.getNode(index).value


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addNode(self.head, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addNode(self.tail.prev, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return None

        self.addNode(self.getNode(index).prev, val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return None

        self.removeNode(self.getNode(index))



# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 128 ms (92.44%)
# Memory Usage: 15.6 MB (59.42%)

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
print(obj.get(0) == -1)

obj.addAtHead(2)
print(obj.get(0) == 2)
# [2]

obj.addAtHead(1)
# [1, 2]
print(obj.get(0) == 1)

obj.addAtTail(4)
# [1, 2, 4]
print(obj.get(2) == 4)

obj.addAtIndex(0, 0)
# [0, 1, 2, 4]
print(obj.get(0) == 0)
print(obj.get(1) == 1)

obj.addAtIndex(3, 3)
# [0, 1, 2, 3, 4]
print(obj.get(3) == 3)

obj.addAtIndex(5, 5)
# [0, 1, 2, 3, 4, 5]
print(obj.get(5) == 5)

obj.deleteAtIndex(0)
# [1, 2, 3, 4, 5]
print(obj.get(0) == 1)

obj.deleteAtIndex(5)
# [1, 2, 3, 4, 5]
print(obj.get(4) == 5)

obj.deleteAtIndex(4)
# [1, 2, 3, 4]
print(obj.get(3) == 4)

obj.deleteAtIndex(2)
# [1, 2, 3, 4]
print(obj.get(2) == 4)