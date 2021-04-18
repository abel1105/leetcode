# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                length += 1
                continue
            if length != 0:
                nums[i - length] = nums[i]

        if length == 0:
            return None

        while length > 0:
            nums[len(nums) - length] = 0
            length -= 1

        return None


# Time complexity: O(n)
# Space Complexity: O(1)
# Runtime: 44 ms (91.17%)
# Memory Usage: 15.5 MB (%)

solution0 = Solution()
nums0 = [0, 1, 0, 3, 12]
solution0.moveZeroes(nums0)
print(nums0 == [1, 3, 12, 0, 0])
solution1 = Solution()
nums1 = [0]
solution1.moveZeroes(nums1)
print(nums1 == [0])
solution2 = Solution()
nums2 = [1, 2, 0, 0, 0, 4]
solution2.moveZeroes(nums2)
print(nums2 == [1, 2, 4, 0, 0, 0])
