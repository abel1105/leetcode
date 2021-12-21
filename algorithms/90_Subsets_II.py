# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        nums = sorted(nums)

        prev = None
        start = 0

        for num in nums:

            if prev != num:
                start = 0

            end = len(ans)

            for i in range(start, end):
                temp = list(ans[i])
                temp.append(num)
                ans.append(temp)
            prev = num
            start = end

        return ans

# Time complexity: O(N * 2 ^ N)
# Space Complexity: O(1)
# Runtime: 28 ms (98.20%)
# Memory Usage: 14.5 MB (28.07%)
