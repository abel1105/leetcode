# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bucket = set()
        for i in nums1:
            bucket.add(i)

        result = []
        for i in nums2:
            if i in bucket:
                result.append(i)
                bucket.remove(i)

        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 68 ms (22.81%)
# Memory Usage: 14.5 MB (%)
