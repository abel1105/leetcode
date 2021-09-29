# Input: nums = [1,2,3,1]
# Output: true
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bucket = set()
        for i in nums:
            if i in bucket:
                return True
            bucket.add(i)
        return False

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 116 ms (84.36%)
# Memory Usage: 20.1 MB (36.04%)
