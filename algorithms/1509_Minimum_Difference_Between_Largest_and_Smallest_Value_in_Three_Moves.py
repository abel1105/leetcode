# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: Change the array [5,3,2,4] to [2,2,2,2].
# The difference between the maximum and minimum is 2-2 = 0.
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if len(nums) <= 4:
            return 0

        start = 0
        end = len(nums) - 4
        result = float('inf')

        while start < end < len(nums):
            diff = nums[end] - nums[start]
            result = min(result, diff)
            end += 1
            start += 1

        return result

# Time complexity: O(NlogN)
# Space Complexity: O(1)
# Runtime: 358 ms (41.93%)
# Memory Usage: 24.1 MB (74.92%)
