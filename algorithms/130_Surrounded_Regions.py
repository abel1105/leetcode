# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for i in range(len(board)):
            self.dfs(board, i, 0)
            self.dfs(board, i, len(board[0]) - 1)

        for j in range(len(board[0])):
            self.dfs(board, 0, j)
            self.dfs(board, len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '@':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

        return board

    def dfs(self, board, i, j):
        if board[i][j] == 'O':
            board[i][j] = '@'
            for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                I, J = i + x, j + y
                if 0 <= I < len(board) and 0 <= J < len(board[0]) and board[I][J] == 'O':
                    self.dfs(board, I, J)

# Time complexity: O(MN)
# Space Complexity: O(MN)
# Runtime: 136 ms (72.37%)
# Memory Usage: 16.1 MB (64.67%)
