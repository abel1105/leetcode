# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for index, val in enumerate(nums):
            if val in bucket:
                if bucket[val] != index:
                    return [index, bucket[val]]
            else:
                bucket[target - val] = index

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 52 ms (97.13%)
# Memory Usage: 15.7 MB (0%)
