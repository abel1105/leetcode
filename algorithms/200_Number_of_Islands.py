# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
from typing import List

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))
                    self.markIslandAsWater(grid, queue)
                    counter += 1

        return counter

    def markIslandAsWater(self, grid, queue):
        while queue:
            (ri, rj) = queue.popleft()
            for i, j in [(ri - 1, rj), (ri + 1, rj), (ri, rj - 1), (ri, rj + 1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i, j))

# Time complexity: O(MxN)
# Space Complexity: O(M*N)
# Runtime: 328 ms (48.41%)
# Memory Usage: 16.7 MB (70.82%)
