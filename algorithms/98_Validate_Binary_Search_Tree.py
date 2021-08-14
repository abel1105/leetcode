# Input: root = [2,1,3]
# Output: true
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root)

    def check(self, root: TreeNode, min=None, max=None) -> bool:
        if not root:
            return True
        if min != None and min >= root.val:
            return False
        if max != None and max <= root.val:
            return False

        return self.check(root.left, min, root.val) and self.check(root.right, root.val, max)

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 48 ms (39.27%)
# Memory Usage: 16.5 MB (33.12%)
