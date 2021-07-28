# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
        if node.right:
            result = self.traversal(node.right, result)
        result.append(node.val)

        return result

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.traversal(root, [])

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 32ms (61.77%)
# Memory Usage: 14.4MB (%)
