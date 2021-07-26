# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        while cur:
            new_cur = cur.next.next
            if new_cur:
                cur.next.next = new_cur.next
            cur = new_cur

        return head.next

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 36 ms (69.39%)
# Memory Usage: 15.1 MB (42.72%)
