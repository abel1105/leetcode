# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
        if node.left:
            result = self.traversal(node.left, result)
        result.append(node.val)
        if node.right:
            result = self.traversal(node.right, result)

        return result

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.traversal(root, [])

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 24ms (95.75%)
# Memory Usage: 14.3MB (46.63%)
