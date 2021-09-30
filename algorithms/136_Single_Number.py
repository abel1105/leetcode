# Input: nums = [2,2,1]
# Output: 1
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bucket = set()
        for i in nums:
            if i in bucket:
                bucket.remove(i)
            else:
                bucket.add(i)

        for i in bucket:
            return i

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 136 ms (59.50%)
# Memory Usage: 1637 MB (%)
