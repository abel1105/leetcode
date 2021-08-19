#
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.areas = [set() for _ in range(9)]
        self.columns = [set() for _ in range(9)]
        self.rows = [set() for _ in range(9)]

        self.collect()
        self.backtrack(0, 0)


    def collect(self):
        for r, row in enumerate(self.board):
            for c, n in enumerate(row):
                if n is not ".":
                    self.rows[r].add(n)
                    self.columns[c].add(n)
                    self.areas[r // 3 * 3 + c // 3].add(n)

    def check(self, r, c, n):
        return n not in self.rows[r] and n not in self.columns[c] and n not in self.areas[r // 3 * 3 + c // 3]

    def put(self, r, c, n):
        self.rows[r].add(n)
        self.columns[c].add(n)
        self.areas[r // 3 * 3 + c // 3].add(n)
        self.board[r][c] = n

    def remove(self, r, c, n):
        self.rows[r].remove(n)
        self.columns[c].remove(n)
        self.areas[r // 3 * 3 + c // 3].remove(n)
        self.board[r][c] = '.'

    def backtrack(self, row, column):
        if row > 8:
            return True
        if column > 8:
            return self.backtrack(row + 1, 0)
        if self.board[row][column] is not '.':
            return self.backtrack(row, column + 1)

        for i in range(1, 10):
            number = str(i)
            if self.check(row, column, number):
                self.put(row, column, number)

                if self.backtrack(row, column + 1):
                    return True
                self.remove(row, column, number)

        return False

# Time complexity: O(9^(N*N))
# Space Complexity: O(N*N)
# Runtime: 232 ms (56.46%)
# Memory Usage: 14.5 MB (28.24%)