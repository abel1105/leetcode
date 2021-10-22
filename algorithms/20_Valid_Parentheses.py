# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        bucket = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if i in bucket:
                if len(stack) == 0 or stack[-1] != bucket[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 42 ms (34.07%)
# Memory Usage: 14.3 MB (64.07%)
