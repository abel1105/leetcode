# Input: root = [1,null,2,3]
# Output: [1,2,3]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node: TreeNode, result):
        if not node:
            return result
        result.append(node.val)
        if node.left:
            result = self.traversal(node.left, result)
        if node.right:
            result = self.traversal(node.right, result)

        return result

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.traversal(root, [])

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 20 ms (99.36%)
# Memory Usage: 14.3 MB (45.99%)
