# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [0] * len(nums)

        dp[0] = nums[0]

        if len(nums) == 1:
            return dp[0]

        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 32 ms (65.92%)
# Memory Usage: 14.4 MB (%)
