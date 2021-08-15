#
from typing import List


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#
#         return self.searchMatrixRange(matrix, target, 0, m - 1, 0, n - 1)
#
#     def searchMatrixRange(self, matrix: List[List[int]], target: int, i_start, i_end, j_start, j_end):
#         if i_start > i_end or j_start > j_end:
#             return False
#
#         pivot = int((j_start + j_end) / 2)
#
#         target_row = i_end + 1
#         for i in range(i_start, i_end + 1):
#             if matrix[i][pivot] == target:
#                 return True
#             if matrix[i][pivot] > target:
#                 target_row = i
#                 break
#
#         # bottomLeft or topRight
#         return self.searchMatrixRange(matrix, target, target_row, i_end, j_start, pivot - 1) or self.searchMatrixRange(matrix, target, i_start, target_row - 1, pivot + 1, j_end)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1

        while i < m and j > -1:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False

# Time complexity: O(M+N)
# Space Complexity: O(1)
# Runtime: 204 ms (10.96%)
# Memory Usage: 20.6 MB (73.35%)
