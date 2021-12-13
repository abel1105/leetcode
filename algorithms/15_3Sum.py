# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for left, v in enumerate(nums[:-2]):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                result = nums[left] + nums[mid] + nums[right]
                if result > 0:
                    right -= 1
                elif result < 0:
                    mid += 1
                else:
                    answer.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return answer

# Time complexity: O(N^2)
# Space Complexity: O(1)
# Runtime: 857 ms (73.97%)
# Memory Usage: 17.4 MB (74.20%)
