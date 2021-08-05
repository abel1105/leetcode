# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                result.append('#')

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        list = data.split(',')
        head = TreeNode(int(list[0]))
        queue = deque([head])
        index = 1
        while queue:
            node = queue.popleft()
            if list[index] is not '#':
                node.left = TreeNode(int(list[index]))
                queue.append(node.left)
            index += 1
            if list[index] is not '#':
                node.right = TreeNode(int(list[index]))
                queue.append(node.right)
            index += 1

        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 108 ms (91.06%)
# Memory Usage: 18.8 MB (79.03%)
