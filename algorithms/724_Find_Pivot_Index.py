# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for key, value in enumerate(nums):
            right -= value
            if left == right:
                return key
            left += value
        return -1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 136 ms (99.13%)
# Memory Usage: 15.5 MB (41.71%)
