#
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        answer = list()

        def backtrack(cur, open, close):
            if len(cur) == 2 * n:
                answer.append(cur)
                return

            if open < n:
                backtrack(cur + '(', open + 1, close)
            if close < open:
                backtrack(cur + ')', open, close + 1)

        backtrack('', 0, 0)

        return answer

# Time complexity: O((4^N)/N^(1/2))
# Space Complexity: O((4^N)/N^(1/2))
# Runtime: 32 ms (85.18%)
# Memory Usage: 14.5 MB (88.19%)
