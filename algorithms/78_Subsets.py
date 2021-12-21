# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            for i in range(len(ans)):
                temp = list(ans[i])
                temp.append(num)
                ans.append(temp)

        return ans

# Time complexity: O(n * 2^n)
# Space Complexity: O(1)
# Runtime: 24 ms (98.99%)
# Memory Usage: 14.4 MB (52.29%)
