# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node and node.left:
                node.left.next = node.right
                node.right.next = node.next.left if node.next else None
                queue.append(node.left)
                queue.append(node.right)
            else:
                break

        return root

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 56 ms (93.17%)
# Memory Usage: 15.7 MB (33.12%)
