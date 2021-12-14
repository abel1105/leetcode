# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        start = 0
        end = 0
        cur = 1
        result = 0
        while end < len(nums):
            cur *= nums[end]
            while cur >= k:
                cur /= nums[start]
                start += 1
            result += end - start + 1
            end += 1

        return result

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 732 ms (49.58%)
# Memory Usage: 17 MB (6.79%)
