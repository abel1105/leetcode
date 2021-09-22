# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = 0
        total = 0
        result = n + 1
        while end < n:
            total += nums[end]
            end += 1
            while total >= target:
                result = min(result, end - start)
                total -= nums[start]
                start += 1

        return 0 if result == n + 1 else result

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 64 ms (98.04%)
# Memory Usage: 16.5 MB (93.55%)
