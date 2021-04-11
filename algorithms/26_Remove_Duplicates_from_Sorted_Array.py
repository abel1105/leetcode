# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = length = 0
        while index < len(nums):
            if nums[length] != nums[index]:
                length += 1
                nums[length] = nums[index]
            index += 1
        return length + 1


# Time complexity: O(n)
# Space Complexity: O(1)
# Runtime: 76 ms (91.52%)
# Memory Usage: 16 MB (51.55%)

solution0 = Solution()
nums0 = [1, 1, 2]
print(solution0.removeDuplicates(nums0) == 2)
print(nums0[0:2] == [1, 2])

solution1 = Solution()
nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution1.removeDuplicates(nums1) == 5)
print(nums1[0:5] == [0, 1, 2, 3, 4])