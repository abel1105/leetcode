# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.max = 1
        self.recursive(root, 1)
        return self.max

    def recursive(self, node, level):
        if level > self.max:
            self.max = level
        for child in node.children:
            self.recursive(child, level + 1)

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 49 ms (18.6%)
# Memory Usage: 16 MB (79.52%)
