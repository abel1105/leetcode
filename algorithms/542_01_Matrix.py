#
from typing import List

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        queue = deque([])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))

        while queue:
            (x, y) = queue.popleft()
            for (x1, y1) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newX, newY = x + x1, y + y1
                if 0 <= newX < len(mat) and 0 <= newY < len(mat[0]) and (newX, newY) not in visited:
                    mat[newX][newY] = mat[x][y] + 1
                    visited.add((newX, newY))
                    queue.append((newX, newY))

        return mat

# Time complexity: O(R*C)
# Space Complexity: O(R*C)
# Runtime: 772 ms (51.91%)
# Memory Usage: 17.3 MB (41.69%)
