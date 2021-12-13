# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            start = 0
            end = len(matrix[0]) - 1
            if matrix[i][start] <= target <= matrix[i][end]:
                while start <= end:
                    mid = (start + end) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1
                break

        return False

# Time complexity: O(logN)
# Space Complexity: O(1)
# Runtime: 36 ms (95.89%)
# Memory Usage: 14.8 MB (35.70%)
