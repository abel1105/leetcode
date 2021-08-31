# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        return root

# Time complexity: O(H)
# Space Complexity: O(1)
# Runtime: 140 ms (36.58%)
# Memory Usage: 16.8 MB (%)
