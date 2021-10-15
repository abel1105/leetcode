# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]  # add 1 for start from 0
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        for i in counter:
            bucket[counter[i]].append(i)

        result = []

        for i in range(len(bucket) - 1, -1, -1):
            for item in bucket[i]:
                result.append(item)
                if len(result) == k:
                    return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 104 ms (62.99%)
# Memory Usage: 19.9 MB (%)
