# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        isTen = False
        front = l1 = ListNode(0, l1)
        l2 = ListNode(0, l2)
        while l1.next or (l2 and l2.next) or isTen:
            first = l1.next.val if l1.next else 0
            second = l2.next.val if l2 and l2.next else 0
            total = first + second + (1 if isTen else 0)
            isTen = total >= 10
            total = total % 10

            if l1.next:
                l1.next.val = total
            else:
                l1.next = ListNode(total, None)

            l1 = l1.next
            l2 = l2.next if l2 else None

        return front.next



# Time complexity: O(max(m,n))
# Space Complexity: O(max(m,n))
# Runtime: 68 ms (76.24%)
# Memory Usage: 14.5 MB (%)

def printVal(node: ListNode) -> str:
    other = ',' + printVal(node.next) if node.next else ''
    return str(node.val) + other

i0 = ListNode(2)
i1 = ListNode(4)
i2 = ListNode(3)
i0.next = i1
i1.next = i2

j0 = ListNode(5)
j1 = ListNode(6)
j2 = ListNode(4)
j0.next = j1
j1.next = j2

solution0 = Solution()
print(printVal(solution0.addTwoNumbers(i0, j0)) == '7,0,8')

i0 = ListNode(9)

j0 = ListNode(9)
j1 = ListNode(9)
j2 = ListNode(9)
j0.next = j1
j1.next = j2

solution0 = Solution()
print(printVal(solution0.addTwoNumbers(i0, j0)) == '8,0,0,1')