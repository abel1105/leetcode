#
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        result = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                result = True
                break

        return result


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 56 ms (52.85%)
# Memory Usage: 17.8 MB (21.69%)

solution0 = Solution()

item0 = ListNode(0)
item1 = ListNode(1)
item2 = ListNode(2)
item0.next = item1
item1.next = item2
item2.next = item1

print(solution0.hasCycle(item0) == True)
