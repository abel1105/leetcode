# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = int(len(nums) / 2)

        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:])
        return self.merge_and_sort(left, right)

    def merge_and_sort(self, left: List[int], right: List[int]) -> List[int]:
        left_index = right_index = 0
        result = []
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])

        return result

# Time complexity: O(NlogN)
# Space Complexity: O(N)
# Runtime: 991 ms (14.34%)
# Memory Usage: 22.3 MB (34.86%)
