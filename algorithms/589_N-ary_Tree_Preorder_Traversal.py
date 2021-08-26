# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        queue = deque([root])
        while queue:
            node = queue.pop()
            if not node:
                continue
            result.append(node.val)
            for child in node.children[::-1]:
                queue.append(child)

        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 56 ms (22.86%)
# Memory Usage: 16.1 MB (64.85%)
