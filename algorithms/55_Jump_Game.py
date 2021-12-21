# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1

        for i in range(last - 1, -1, -1):
            if i + nums[i] >= last:
                last = i

        return last == 0

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 444 ms (99.55%)
# Memory Usage: 15.2 MB (71.23%)
