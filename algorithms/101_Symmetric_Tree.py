# Input: root = [1,2,2,3,4,4,3]
# Output: true
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque([root, root])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            queue.extend([t1.left, t2.right])
            queue.extend([t1.right, t2.left])
        return True

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 36 ms (60.19%)
# Memory Usage: 14.2 MB (78.76%)
