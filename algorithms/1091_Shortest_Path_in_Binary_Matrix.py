# Input: grid = [[0,1],[1,0]]
# Output: 2
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        seen = set([(0, 0)])
        queue = deque([(0, 0, 1)])

        while queue:
            (i, j, count) = queue.popleft()
            if i == n -1 and j == n - 1:
                return count
            for (x, y) in [(1, 1), (1, 0), (0, 1), (1, -1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                I, J = i + x, j + y
                if 0 <= I < n and 0 <= J < n and grid[I][J] == 0 and (I, J) not in seen:
                    seen.add((I, J))
                    queue.append((I, J, count + 1))

        return -1


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 693 ms (60.12%)
# Memory Usage: 15.5 MB (41.00%)