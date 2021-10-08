# Input: nums = [1,2,3,1], k = 3
# Output: true
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        bucket = {}
        for key, i in enumerate(nums):
            if i in bucket:
                if abs(bucket[i] - key) <= k:
                    return True
            bucket[i] = key

        return False

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 612 ms (65.86%)
# Memory Usage: 27.7 MB (70.05%)
