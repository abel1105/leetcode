# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while start < end:
            s[end], s[start] = s[start], s[end]
            start += 1
            end -= 1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 192 ms (89.23%)
# Memory Usage: 18.8 MB (20.68%)
