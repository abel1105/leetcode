# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        front = c1 = ListNode(0, l1)
        c2 = ListNode(0, l2)

        while c1.next and c2.next:
            if c1.next.val <= c2.next.val:
                c1 = c1.next
            else:
                temp = c2.next
                c2.next = c2.next.next
                temp.next = c1.next
                c1.next = temp

        if c2.next:
            c1.next = c2.next

        return front.next

    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val >= l2.val:
            l2.next = self.mergeTwoListsRecursive(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28ms (98.21%)
# Memory Usage: 14.2MB (83.69%)

def printVal(node: ListNode) -> str:
    other = ',' + printVal(node.next) if node.next else ''
    return str(node.val) + other


solution0 = Solution()
print(solution0.mergeTwoLists(None, None) == None)

i0 = ListNode(1)
i1 = ListNode(2)
i2 = ListNode(3)
i0.next = i1
i1.next = i2

j0 = ListNode(1)
j1 = ListNode(2)
j2 = ListNode(3)
j0.next = j1
j1.next = j2

solution1 = Solution()
print(printVal(solution1.mergeTwoLists(i0, j0)) == '1,1,2,2,3,3')
