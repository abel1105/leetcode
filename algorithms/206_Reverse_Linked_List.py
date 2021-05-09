# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        head = ListNode(0, head)
        current = head.next
        while current and current.next:
            temp = current.next
            current.next = temp.next
            temp.next = head.next
            head.next = temp
        return head.next


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 36 ms (61.45%)
# Memory Usage: 15.5 MB (75.02%)

solution0 = Solution()

item0 = ListNode(1)
item1 = ListNode(2)
item2 = ListNode(3)
item0.next = item1
item1.next = item2

head = solution0.reverseList(item0)
print(head.val)
print(head.next.val)
print(head.next.next.val)