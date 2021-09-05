# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1

    def dfs(self, node):
        if not node:
            return 0
        left = 0
        right = 0
        if node.left:
            left = self.dfs(node.left)
        if node.right:
            right = self.dfs(node.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1

        return max(left, right) + 1

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 46 ms (83.54%)
# Memory Usage: 18 MB (87.94%)
