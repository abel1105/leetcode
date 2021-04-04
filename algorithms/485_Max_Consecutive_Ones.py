# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                if current > max:
                    max = current
                current = 0
        # if the last time current is the max then you have to return the current
        return current if current > max else max


# Time complexity: O(n)
# Runtime: 340 ms (86.07%)
# Memory Usage: 14.3 MB


solution0 = Solution()
print(solution0.findMaxConsecutiveOnes([0]) == 0)
solution1 = Solution()
print(solution1.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 0, 0, 0]) == 2)
solution2 = Solution()
print(solution2.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 1, 1, 1]) == 4)
