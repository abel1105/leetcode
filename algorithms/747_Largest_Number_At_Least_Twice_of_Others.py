# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxInd = None
        secInd = None
        for key, value in enumerate(nums):
            if (secInd is None or value > nums[secInd]) and (maxInd is not None and value < nums[maxInd]):
                secInd = key
            elif (maxInd is None or value > nums[maxInd]):
                secInd = maxInd
                maxInd = key

        if maxInd is not None and secInd is not None and nums[maxInd] >= nums[secInd] * 2:
            return maxInd
        if maxInd is not None and secInd is None:
            return maxInd
        return -1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28ms (95.33%)
# Memory Usage: 14.2 MB (40.85%)
