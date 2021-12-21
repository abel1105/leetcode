# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrack(resume, path):
            if len(path) == len(nums):
                ans.append(list(path))
                return

            for i in range(len(resume)):
                if i > 0 and resume[i] == resume[i - 1]:
                    continue
                backtrack(resume[:i] + resume[i + 1:], path + [resume[i]])

        backtrack(nums, [])

        return ans

# Time complexity: O(N * N!)
# Space Complexity: O(N^2)
# Runtime: 60 ms (69.45%)
# Memory Usage: 14.8 MB (16.16%)
