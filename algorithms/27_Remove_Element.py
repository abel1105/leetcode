# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[length] = nums[index]
                length += 1
        return length

# Time complexity: 32 ms O(n)
# Space Complexity: O(1)
# Runtime: 32 ms (72.58%)
# Memory Usage: 14.2 MB (75.79%)

solution0 = Solution()
nums0 = [3, 2, 2, 3]
print(solution0.removeElement(nums0, 3) == 2)
print(3 not in nums0[0:2])

solution1 = Solution()
nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
print(solution1.removeElement(nums1, 2) == 5)
print(2 not in nums1[0:5])

solution2 = Solution()
nums2 = [2, 2, 2]
print(solution2.removeElement(nums2, 2) == 0)
print(2 not in nums2[0:0])

solution3 = Solution()
nums3 = []
print(solution3.removeElement(nums3, 0) == 0)
print(0 not in nums3[0:0])

solution4 = Solution()
nums4 = [4, 5]
print(solution3.removeElement(nums4, 4) == 1)
print(4 not in nums4[0:1])
