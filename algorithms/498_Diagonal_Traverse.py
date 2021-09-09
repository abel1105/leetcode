# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        line = {}
        for row in range(m):
            for column in range(n):
                if row + column not in line:
                    line[row + column] = [mat[row][column]]
                else:
                    line[row + column].append(mat[row][column])

        result = []
        for i in range(m + n - 1):
            if i % 2 == 0:
                result.extend(line[i][::-1])
            else:
                result.extend(line[i])
        return result

# Time complexity: O(N*M)
# Space Complexity: O(N*M)
# Runtime: 196 ms (61.64%)
# Memory Usage: 17.1 MB (28.63%)
