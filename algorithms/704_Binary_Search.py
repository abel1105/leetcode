# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


# Time complexity: O(logN)
# Space Complexity: O(1)
# Runtime: 228 ms (93.41%)
# Memory Usage: 15.7 MB (%)