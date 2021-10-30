# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.image = image
        self.dfs(sr, sc, self.image[sr][sc], newColor)
        return self.image


    def dfs(self, sr, sc, oldColor, newColor):
        self.image[sr][sc] = newColor

        for (x,y) in [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]:
            if 0 <= x < len(self.image) and 0 <= y < len(self.image[0]) and self.image[x][y] == oldColor:
                self.dfs(x, y, oldColor, newColor)


# Time complexity: O(MN)
# Space Complexity: O(MN)
# Runtime: 76 ms (75.67%)
# Memory Usage: 14.4 MB (77.98%)
