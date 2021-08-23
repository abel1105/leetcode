# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.nums = nums
        self.backtrack([], result)

        return result

    def backtrack(self, cur, result):
        if len(cur) == len(self.nums):
            result.append(list(cur))
            return
        for i in range(0, len(self.nums)):
            if self.nums[i] not in cur:
                cur.append(self.nums[i])
                self.backtrack(cur, result)
                cur.pop()

# Time complexity: O(N^2)
# Space Complexity: O(N^2)
# Runtime: 32 ms (96.69%)
# Memory Usage: 14.6 MB (%)
