# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        dp = [0] * n

        if nums[1] - nums[0] == nums[2] - nums[1]:
            dp[2] = 1

        result = dp[2]

        for i in range(3, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1

            result += dp[i]

        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 32 ms (92.21%)
# Memory Usage: 14.5 MB (75.02%)
