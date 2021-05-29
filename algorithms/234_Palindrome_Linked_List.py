# Input: head = [1,2,2,1]
# Output: true


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        reverse = None

        while fast and fast.next:
            temp = slow

            slow = slow.next
            fast = fast.next.next

            temp.next = reverse
            reverse = temp
        # Move to next number if even number
        # 1 -> 2 -> 3(origin) -> 2(move here) -> 1
        if fast:
            slow = slow.next

        while reverse:
            if slow.val != reverse.val:
                return False
            reverse = reverse.next
            slow = slow.next
        return True


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 672 ms (96.04%)
# Memory Usage: 31.4 MB (98.10%)

item0 = ListNode(1)
item1 = ListNode(2)
item2 = ListNode(2)
item3 = ListNode(1)
item0.next = item1
item1.next = item2
item2.next = item3

solution0 = Solution()
print(solution0.isPalindrome(item0) == True)
