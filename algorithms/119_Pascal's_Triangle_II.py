# Input: rowIndex = 3
# Output: [1,3,3,1]
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)

        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                result[j] += result[j - 1]

        return result

# Time complexity: O(k^2)
# Space Complexity: O(k)
# Runtime: 32 ms (62.16%)
# Memory Usage: 14.2 MB (78.09%)
