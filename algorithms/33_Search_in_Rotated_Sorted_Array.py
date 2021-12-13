# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

# Time complexity: O(logN)
# Space Complexity: O(1)
# Runtime: 44 ms (51.81%)
# Memory Usage: 14.6 MB (56.35%)
