# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head

        cur = head
        length = 0
        while cur:
            length += 1
            if not cur.next:
                break
            cur = cur.next

        remain = k % length
        if remain == 0:
            return head

        cur.next = head
        cur = head
        for i in range(length - remain - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None

        return new_head

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 32ms (92.12%)
# Memory Usage: 14.2MB (59.13%)
