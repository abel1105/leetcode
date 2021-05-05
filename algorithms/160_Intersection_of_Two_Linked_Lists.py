# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        first = headA
        second = headB

        while first != second:
            first = headB if not first else first.next
            second = headA if not second else second.next

        return first


# Time Complexity: O(N)
# Space Complexity: O(1)
# Runtime: 164 ms (53.11%)
# Memory Usage: 29.3 MB (92.81%)


solution0 = Solution()

item0 = ListNode(0)
item1 = ListNode(1)
item2 = ListNode(2)
item3 = ListNode(3)
item4 = ListNode(4)
item0.next = item1
item1.next = item2
item2.next = item3
item4.next = item2

print(solution0.getIntersectionNode(item0, item4).val == 2)
