# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
#
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]


class Node:
    def __init__(self, key, val, nextNode = None):
        self.key = key
        self.val = val
        self.next = nextNode


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.bucket = [None] * self.size

    def get_hash(self, key):
        return key % self.size


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash = self.get_hash(key)
        if self.bucket[hash] == None:
            self.bucket[hash] = Node(key, value)
        else:
            head = self.bucket[hash]
            while head:
                if head.key == key:
                    head.val = value
                    break
                elif head.next == None:
                    head.next = Node(key, value)
                    break
                head = head.next

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash = self.get_hash(key)
        if self.bucket[hash] == None:
            return -1

        head = self.bucket[hash]
        while head:
            if head.key == key:
                return head.val
            else:
                head = head.next

        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash = self.get_hash(key)
        if self.bucket[hash] == None:
            return

        head = node = Node(0, 0, self.bucket[hash])
        while node:
            if node.next and node.next.key == key:
                node.next = node.next.next
                break
            node = node.next

        self.bucket[hash] = head.next


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 244 ms (74.59 %)
# Memory Usage: 17.5 MB (56.89 %)