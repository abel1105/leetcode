# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,
# 0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,
# 1,0,0,0,0]] Output: 6 Explanation: The answer is not 11, because the island must be connected 4-directionally.
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    s = self.dfs(grid, i, j, 0)
                    max_sum = max(max_sum, s)

        return max_sum

    def dfs(self, grid, i, j, s):
        grid[i][j] = 0
        s += 1
        for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i = i + x
            new_j = j + y
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                s = self.dfs(grid, new_i, new_j, s)

        return s

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 112 ms (99.55%)
# Memory Usage: 16.5 MB (60.49%)
