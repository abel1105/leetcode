# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        ans_start = -1
        ans_end = -1
        while start < len(nums):
            if nums[start] > target:
                break
            if nums[start] == target:
                if ans_start == -1:
                    ans_start = start
                ans_end = start
            start += 1

        return [ans_start, ans_end]

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 84 ms (75.90%)
# Memory Usage: 15.4 MB (83.45%)
