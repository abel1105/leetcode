# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd = head
        middle = even = head.next

        while even and even.next:
            odd.next = even.next
            even.next = even.next.next  # maybe None
            odd = odd.next
            even = even.next

        odd.next = middle
        return head


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 40 ms (81.68%)
# Memory Usage: 16.3 MB (57.64%)

item0 = ListNode(1)
item1 = ListNode(2)
item2 = ListNode(3)
item3 = ListNode(4)
item4 = ListNode(5)
item0.next = item1
item1.next = item2
item2.next = item3
item3.next = item4

solution0 = Solution()
answer = solution0.oddEvenList(item0)
print(answer.val == 1)
print(answer.next.val == 3)
print(answer.next.next.val == 5)
print(answer.next.next.next.val == 2)
print(answer.next.next.next.next.val == 4)
print(answer.next.next.next.next.next == None)
