#
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.bucket = {}
        self.result = []
        self.traverse(root)

        return self.result

    def traverse(self, node):
        if not node:
            return '#'
        key = str(node.val) + '#' + self.traverse(node.left) + '#' + self.traverse(node.right)
        if key in self.bucket:
            if self.bucket[key]:
                self.result.append(node)
                self.bucket[key] = False
        else:
            self.bucket[key] = True
        return key

# Time complexity: O(N^2)
# Space Complexity: O(N^2)
# Runtime: 101 ms (34.73%)
# Memory Usage: 23 MB (58.92%)
