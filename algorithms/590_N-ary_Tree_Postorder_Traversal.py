# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]
from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([(root, False)])
        while queue:
            node, isTraverse = queue.pop()
            if node.children and not isTraverse:
                queue.append((node, True))
                for child in node.children[::-1]:
                    queue.append((child, False))
            else:
                result.append(node.val)
        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 52 ms (58.19%)
# Memory Usage: 16.2 MB (%)
