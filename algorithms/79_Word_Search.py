# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = '#'
                    self.backtrack(1, i, j, board, word)
                    board[i][j] = temp
                    if self.result:
                        return self.result

        return self.result

    def backtrack(self, start, i, j, board, word):
        if start >= len(word):
            self.result = True
            return

        for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            I, J = i + x, j + y
            if 0 <= I < len(board) and 0 <= J < len(board[0]) and board[I][J] == word[start]:
                temp = board[I][J]
                board[I][J] = '#'
                self.backtrack(start + 1, I, J, board, word)
                board[I][J] = temp
                if self.result:
                    return

# Time complexity: O(M * N * 3^k)
# Space Complexity: O(k)
# Runtime: 5360 ms (82.63%)
# Memory Usage: 14.4 MB (%)
