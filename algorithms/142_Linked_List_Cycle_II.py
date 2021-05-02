# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        fast = head
        slow = head
        meet = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                meet = fast
                break

        if not meet:
            return None

        if meet == head:
            return head

        while meet != head:
            meet = meet.next
            head = head.next

        return meet

# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 52 ms (53.07%)
# Memory Usage: 17.3 MB (23.97%)


solution0 = Solution()

item0 = ListNode(0)
item1 = ListNode(1)
item2 = ListNode(2)
item0.next = item1
item1.next = item2
item2.next = item1


print(solution0.detectCycle(item0) == item1)








