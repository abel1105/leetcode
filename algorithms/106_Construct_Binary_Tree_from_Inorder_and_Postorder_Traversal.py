# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.inorder_dict = {}
        self.postorder = []

    def build(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None

        root = TreeNode(self.postorder.pop())
        mid = self.inorder_dict[root.val]
        # right before left, because post order is (left, right, root)
        root.right = self.build(mid + 1, end)
        root.left = self.build(start, mid - 1)
        return root


    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        for index, value in enumerate(inorder):
            self.inorder_dict[value] = index
        self.postorder = postorder

        return self.build(0, len(inorder) - 1)


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 60 ms (72.60%)
# Memory Usage: 18.1 MB (98.11%)
