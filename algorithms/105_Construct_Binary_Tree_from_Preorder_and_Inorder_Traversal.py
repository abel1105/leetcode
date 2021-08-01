# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_dict = {}
        preorder_queue = deque(preorder)
        for index, value in enumerate(inorder):
            inorder_dict[value] = index

        def dfs(start, end):
            if start > end:
                return None

            root = TreeNode(preorder_queue.popleft())
            mid = inorder_dict[root.val]
            root.left = dfs(start, mid - 1)
            root.right = dfs(mid + 1, end)
            return root

        return dfs(0, len(preorder) - 1)

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 56 ms (90.97%)
# Memory Usage: 18.7 MB (88.49%)
