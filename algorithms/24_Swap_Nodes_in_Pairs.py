# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        temp = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = self.swapPairs(temp)

        return new_head

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 32ms (63.56%)
# Memory Usage: 14.3MB (%)
