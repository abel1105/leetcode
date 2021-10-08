# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        bucket = {}
        for i in nums1:
            if i in bucket:
                bucket[i] += 1
            else:
                bucket[i] = 1

        result = []
        for i in nums2:
            if i in bucket and bucket[i] > 0:
                bucket[i] -= 1
                result.append(i)

        return result


# Time complexity: O(max len(n1, n2))
# Space Complexity: O(union(n1, n2))
# Runtime: 48 ms (76.31%)
# Memory Usage: 14.4 MB (40.55%)