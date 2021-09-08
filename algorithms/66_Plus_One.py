# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        isTen = False
        isLast = True
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            if isLast:
                num += 1
                isLast = False
            if isTen:
                num += 1
                isTen = False
            if num >= 10:
                isTen = True
                digits[i] = 0
            else:
                digits[i] = num
                break
        if isTen:
            return [1] + digits
        else:
            return digits

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28 ms (89.53%)
# Memory Usage: 14.2 MB (75.46%)
