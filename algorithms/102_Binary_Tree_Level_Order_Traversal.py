# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])

        while queue:
            level_result = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_result)

        return result

# Time complexity: O(n)
# Space Complexity: O(n)
# Runtime: 36 ms (62.95%)
# Memory Usage: 14.7 MB (45.32%)
