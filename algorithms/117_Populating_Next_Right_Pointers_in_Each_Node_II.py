#
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root

        while node:
            dummy = Node(0)
            cur = dummy
            while node:
                if node.left:
                    cur.next = node.left
                    cur = node.left
                if node.right:
                    cur.next = node.right
                    cur = node.right
                node = node.next
            node = dummy.next

        return root

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 40 ms (97.25%)
# Memory Usage: 15.3 MB (80.92%)
