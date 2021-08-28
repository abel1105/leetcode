#
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level = []
            for _ in range(0, len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            result.append(level)
        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 89 ms (%)
# Memory Usage: 15.9 MB (82.60%)
