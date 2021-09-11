# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        row = 0
        column = 0
        level = 0
        direction = 0  # 0: right/ 1: down/ 2: left/ 3: up
        for i in range(m * n):
            result.append(matrix[row][column])
            if direction == 0:
                if column < n - level - 1:
                    column += 1
                else:
                    row += 1
                    direction = 1
            elif direction == 1:
                if row < m - level - 1:
                    row += 1
                else:
                    column -= 1
                    direction = 2
            elif direction == 2:
                if column > level:
                    column -= 1
                else:
                    row -= 1
                    direction = 3
                    level += 1
            else:
                if row > level:
                    row -= 1
                else:
                    column += 1
                    direction = 0

        return result

# Time complexity: O(M*N)
# Space Complexity: O(1)
# Runtime: 41 ms (14.9%)
# Memory Usage: 14.3 MB (57.62%)
