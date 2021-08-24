# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        self.digits = digits

        result = []

        if digits:
            self.backtrack('', 0, result)

        return result

    def backtrack(self, cur, start, result):
        if len(self.digits) == len(cur):
            result.append(cur)
            return

        if start >= len(self.digits):
            return
        number = self.digits[start]

        for i in range(0, len(self.mapping[number])):
            cur += self.mapping[number][i]
            self.backtrack(cur, start + 1, result)
            cur = cur[0:-1]

        return


# Time complexity: O(4^N*N)
# Space Complexity: O(N)
# Runtime: 32 ms (59.31%)
# Memory Usage: 14.1 MB (86.51%)
