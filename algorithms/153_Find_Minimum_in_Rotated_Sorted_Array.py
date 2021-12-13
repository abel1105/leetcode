# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[end]:
                start = mid + 1
            else:
                end = mid

        return nums[start]

# Time complexity: O(logN)
# Space Complexity: O(1)
# Runtime: 40 ms (73.37%)
# Memory Usage: 14.5 MB (85.27%)
