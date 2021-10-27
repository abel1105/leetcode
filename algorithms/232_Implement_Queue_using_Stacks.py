# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
#
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.move()
        return self.s2.pop()

    def move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def peek(self) -> int:
        self.move()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s2 and not self.s1

# Time complexity: O(1)
# Space Complexity: O(N)
# Runtime: 24ms (96.48%)
# Memory Usage: 14.3 MB (71.48%)
