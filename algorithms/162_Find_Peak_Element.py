# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start


# Time complexity: O(logN)
# Space Complexity: O(1)
# Runtime: 48 ms (51.49%)
# Memory Usage: 14.3 MB (72.10%)
