# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            result = numbers[start] + numbers[end]
            if result == target:
                return [start + 1, end + 1]
            elif result > target:
                end -= 1
            else:
                start += 1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 81 ms (33.44%)
# Memory Usage: 95 MB ( 61.87%)
