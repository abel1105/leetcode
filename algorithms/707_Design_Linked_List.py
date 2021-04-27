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
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.length <= index or index < 0:
            return -1
        current = self.head
        while index > 0:
            current = current.next
            index -= 1
        return current.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Item(val, self.head)
        if self.length == 0:
            self.tail = self.head

        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail = Item(val, None)
        if self.length == 0:
            self.head = self.tail = tail
        else:
            self.tail.next = tail
            self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length or index < 0:
            return None
        if index == 0:
            return self.addAtHead(val)
        if index == self.length:
            return self.addAtTail(val)

        current = Item(0, self.head)
        while index > 0:
            current = current.next
            index -= 1

        current.next = Item(val, current.next)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 > index or index >= self.length:
            return None

        current = Item(0, self.head)
        for i in range(index):
            current = current.next

        current.next = current.next.next

        if index == 0:
            self.head = current.next
        if index == self.length - 1:
            self.tail = current
        self.length -= 1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 188 ms (79.40%)
# Memory Usage: 15 MB (59.42%)

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