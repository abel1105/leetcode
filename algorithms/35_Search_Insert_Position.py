# Input: nums = [1,3,5,6], target = 5
# Output: 2
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start

# Time complexity: O(logN)
# Space Complexity: O(1)
# Runtime: 48 ms (78.78%)
# Memory Usage: 15 MB (56.32%)
