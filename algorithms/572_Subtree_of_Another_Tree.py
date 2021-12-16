# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root or not subRoot:
            return False

        if self.isMatch(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatch(self, origin, target):
        if not origin or not target:
            return origin == target
        if origin.val == target.val:
            return self.isMatch(origin.left, target.left) and self.isMatch(origin.right, target.right)
        return False

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 126 ms (87.96%)
# Memory Usage: 15.3 MB (42.87%)
