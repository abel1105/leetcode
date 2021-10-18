# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]
#
# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for i in range(k)]
        self.max = k
        self.size = 0
        self.start = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail = 0 if self.tail + 1 == self.max else self.tail + 1
        self.queue[tail] = value
        self.tail = tail
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        start = 0 if self.start + 1 == self.max else self.start + 1
        value = self.queue[self.start]
        self.queue[self.start] = None
        self.start = start
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max

# Time complexity: O(1)
# Space Complexity: O(N)
# Runtime: 64 ms (93.38%)
# Memory Usage: 15 MB (33.99%)
