# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        self.candidates = candidates
        self.ans = []

        self.backtrack(0, [], target)

        return self.ans

    def backtrack(self, start, path, target):
        if target == 0:
            self.ans.append(list(path))
            return

        if start == len(self.candidates):
            return

        for i in range(start, len(self.candidates)):
            if i > start and self.candidates[i] == self.candidates[i - 1]:
                continue
            if self.candidates[i] > target:
                return

            path.append(self.candidates[i])
            self.backtrack(i + 1, path, target - self.candidates[i])
            path.pop()

# Time complexity: O(2^N)
# Space Complexity: O(1)
# Runtime: 40 ms (96.37%)
# Memory Usage: 14.2 MB (77.89%)
