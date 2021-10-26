# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cache = {}

        def dfs(index, cur):
            if (index, cur) in self.cache:
                return self.cache[(index, cur)]

            if len(nums) == index:
                if cur == 0:
                    return 1
                return 0
            item = nums[index]
            total = dfs(index + 1, cur + item) + dfs(index + 1, cur - item)
            self.cache[(index, cur)] = total
            return total

        return dfs(0, target)

# Time complexity: O(t*n) t refers to the sum of the nums array
# Space Complexity: O(t*n)
# Runtime: 588 ms (18.5%)
# Memory Usage: 36.3 MB (16.03%)
