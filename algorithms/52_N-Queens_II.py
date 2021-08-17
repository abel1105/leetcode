#
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cols = set()
        self.dales = set()
        self.hills = set()
        self.n = n
        return self.backtrack(0, 0)

    def check(self, row, column):
        return column not in self.cols and (row - column) not in self.dales and (row + column) not in self.hills

    def place(self, row, column):
        self.cols.add(column)
        self.dales.add(row - column)
        self.hills.add(row + column)

    def remove(self, row, column):
        self.cols.remove(column)
        self.dales.remove(row - column)
        self.hills.remove(row + column)

    def backtrack(self, row, count):
        if row == self.n:
            return count + 1

        for c in range(self.n):
            if self.check(row, c):
                self.place(row, c)
                count = self.backtrack(row + 1, count)
                self.remove(row, c)

        return count

# Time complexity: O(N!)
# Space Complexity: O(N)
# Runtime: 60 ms (66.13%)
# Memory Usage: 14.2 MB (66.13%)
