# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = second = dummy

        while n and first:
            first = first.next
            n -= 1

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28 ms (92.26%)
# Memory Usage: 14.3 MB (48.85%)

solution0 = Solution()

item0 = ListNode(1)
item1 = ListNode(2)
item2 = ListNode(3)
item3 = ListNode(4)
item4 = ListNode(5)
item0.next = item1
item1.next = item2
item2.next = item3
item3.next = item4

head = solution0.removeNthFromEnd(item0, 2)

print(head.val == 1)
print(head.next.val == 2)
print(head.next.next.val == 3)
print(head.next.next.next.val == 5)

solution1 = Solution()

item0 = ListNode(1)
item1 = ListNode(2)

item0.next = item1
head = solution0.removeNthFromEnd(item0, 2)

print(head.val == 2)









