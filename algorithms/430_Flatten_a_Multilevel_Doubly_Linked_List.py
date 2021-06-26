# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def dfs(self, node: 'Node') -> 'Node':
        current = node
        while current:
            if current.child:
                temp = current.next
                current.next = current.child
                current.child.prev = current
                current.child = None
                current = self.dfs(current.next)
                current.next = temp
                if temp:
                    temp.prev = current

            if not current.next:
                break
            current = current.next
        return current

    def flatten(self, head: 'Node') -> 'Node':

        front = Node(0, None, head, None)

        self.dfs(front.next)

        return front.next

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28ms (95.73%)
# Memory Usage: 14.7MB (63.10%)
