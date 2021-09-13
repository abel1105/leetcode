# Input: a = "11", b = "1"
# Output: "100"
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry % 2)
            carry = carry // 2

        return result[::-1]

# Time complexity: O(max(a,b))
# Space Complexity: O(a+b)
# Runtime: 40 ms (27.99%)
# Memory Usage: 14.3 MB (54.68%)
