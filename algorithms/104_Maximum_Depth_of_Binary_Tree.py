# Input: root = [3,9,20,null,null,15,7]
# Output: 3
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_result = self.maxDepth(root.left)
        right_result = self.maxDepth(root.right)
        return max(left_result, right_result) + 1

# Time complexity: O(n)
# Space Complexity: O(n)
# Runtime: 44 ms (49.66%)
# Memory Usage: 16.1 MB (41.12%)
