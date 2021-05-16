# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = dummy = ListNode(0, head)

        while current:
            fast = current.next
            while fast and fast.val == val:
                fast = fast.next
            current.next = fast
            current = fast

        return dummy.next

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 72 ms (41.44%)
# Memory Usage: 17.2 MB (66.23%)


solution0 = Solution()

item0 = ListNode(0)
item1 = ListNode(1)
item2 = ListNode(2)
item3 = ListNode(3)
item4 = ListNode(2)

item0.next = item1
item1.next = item2
item2.next = item3
item3.next = item4

result = solution0.removeElements(item0, 2)
print(result.val == 0)
print(result.next.val == 1)
print(result.next.next.val == 3)


solution1 = Solution()

item5 = ListNode(5)
item6 = ListNode(5)
item7 = ListNode(5)

item5.next = item6
item6.next = item7

result = solution1.removeElements(item5, 5)
print(result == None)
