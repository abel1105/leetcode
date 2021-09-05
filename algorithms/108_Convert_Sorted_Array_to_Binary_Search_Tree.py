# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if right < left:
                return None
            mid = (right + left) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node

        return helper(0, len(nums) - 1)

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 81 ms (16.45%)
# Memory Usage: 15.8 MB (15.6%)
