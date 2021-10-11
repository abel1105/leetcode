# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxs = [{} for i in range(9)]
        for i, row in enumerate(board):
            for j, text in enumerate(row):
                if text == '.':
                    continue
                key = i // 3 * 3 + j // 3
                if text in rows[i]:
                    return False
                if text in columns[j]:
                    return False
                if text in boxs[key]:
                    return False
                rows[i][text] = True
                columns[j][text] = True
                boxs[key][text] = True

        return True

# Time complexity: O(1)
# Space Complexity: O(1)
# Runtime: 88 ms (96.31%)
# Memory Usage: 14.5 MB (%)
