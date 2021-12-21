# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def simple_rob(start, end):
            include = exclude = 0
            for j in range(start, end):
                i = include
                e = exclude
                include = e + nums[j]
                exclude = max(e, i)
            return max(include, exclude)

        return max(simple_rob(0, len(nums) - 1), simple_rob(1, len(nums)))

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 24 ms (96.64%)
# Memory Usage: 14.1 MB (81.41%)
