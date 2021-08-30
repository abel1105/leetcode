# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAllLeft(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.pushAllLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) is not 0

    def pushAllLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Time complexity: O(1)
# Space Complexity: O(N)
# Runtime: 64 ms (97.95%)
# Memory Usage: 20.6 MB (54.24%)
