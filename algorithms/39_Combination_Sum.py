#
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.ans = []
        self.candidates = candidates
        self.backtrack(0, [], 0)

        return self.ans

    def backtrack(self, start, path, total):
        if total > self.target:
            return

        if total == self.target:
            self.ans.append(list(path))
            return

        for i in range(start, len(self.candidates)):
            path.append(self.candidates[i])
            total += self.candidates[i]
            self.backtrack(i, path, total)
            path.pop()
            total -= self.candidates[i]

# Time complexity: O(k * 2^n')
# Space Complexity: O(N)
# Runtime: 100 ms (44.34%)
# Memory Usage: 14.3 MB (77.90%)
