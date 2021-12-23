# Input: nums = [2,3,1,1,4]
# Output: 2
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # the initial range (after 0th jump) is [0,0]
        l = r = 0
        nJumps = 0
        while r < len(nums) - 1:
            nJumps += 1
            furthest = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, furthest

        return nJumps

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 112 ms (98.33%)
# Memory Usage: 15.2 MB (72.63%)
