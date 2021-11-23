# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = deque([])
        fresh = 0
        minute = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        if fresh == 0:
            return minute

        while rotten:
            is_rotten = False
            for _ in range(len(rotten)):
                (i, j) = rotten.popleft()
                for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                        is_rotten = True
                        fresh -= 1
                        grid[new_i][new_j] = 2
                        rotten.append((new_i, new_j))
            if is_rotten:
                minute += 1

        return -1 if fresh > 0 else minute

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 66 ms (20.02%)
# Memory Usage: 14.3 MB (40.98%)
