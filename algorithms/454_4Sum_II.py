# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        bucket = {}
        for i in nums1:
            for j in nums2:
                if i + j in bucket:
                    bucket[i + j] += 1
                else:
                    bucket[i + j] = 1
        result = 0
        for i in nums3:
            for j in nums4:
                if -1 * (i + j) in bucket:
                    result += bucket[-1 * (i + j)]

        return result

# Time complexity: O(N^2)
# Space Complexity: O(N^2)
# Runtime: 829 ms (51.07%)
# Memory Usage: 14.5 MB (70.75%)
