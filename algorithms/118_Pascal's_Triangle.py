# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            result.append([1])
            for j in range(1, i):
                result[i].append(result[i - 1][j - 1] + result[i - 1][j])
            result[i].append(1)

        return result

# Time complexity: O(k^2)
# Space Complexity: O(k^2)
# Runtime: 35 ms (23.95%)
# Memory Usage: 14.3 MB (%)
