# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Time complexity: O(n)
# Space Complexity: O(n)
# Runtime: 75 ms (48.87%)
# Memory Usage: 16.3 MB (%)
