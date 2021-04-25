# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.
import math
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -math.inf
        second = -math.inf
        third = -math.inf

        for i in range(len(nums)):
            if nums[i] >= first:
                if nums[i] != first:
                    third = second
                    second = first
                first = nums[i]
            elif nums[i] >= second:
                if nums[i] != second:
                    third = second
                second = nums[i]
            elif nums[i] >= third:
                third = nums[i]

        return third if third != -math.inf else first


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 48 ms (86.48%)
# Memory Usage: 15.1 MB (88.18%)

solution0 = Solution()
print(solution0.thirdMax([2, 2, 3, 1]), solution0.thirdMax([2, 2, 3, 1]) == 1)
solution1 = Solution()
print(solution1.thirdMax([3, 2, 1]), solution1.thirdMax([3, 2, 1]) == 1)
solution2 = Solution()
print(solution2.thirdMax([1, 2]), solution2.thirdMax([1, 2]) == 2)
