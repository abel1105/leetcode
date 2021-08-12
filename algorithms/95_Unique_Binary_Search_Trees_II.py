# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateSubtrees(1, n, {})

    def generateSubtrees(self, start: int, end: int, memory: dict) -> List[TreeNode]:
        if start > end:
            return [None]

        if (start, end) in memory:
            return memory[(start, end)]

        result = []

        for i in range(start, end + 1):
            for left in self.generateSubtrees(start, i - 1, memory):
                for right in self.generateSubtrees(i + 1, end, memory):
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    result.append(node)

        memory[(start, end)] = result

        return result

# Time complexity: O(N^2) Not sure
# Space Complexity: O(N)
# Runtime: 52 ms (92.78%)
# Memory Usage: 14.8 MB (96.72%)
