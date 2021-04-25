# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        final = sorted(heights)
        count = 0
        for index in range(len(heights)):
            if heights[index] != final[index]:
                count += 1
        return count


# Time complexity: O(NlogN)
# Space Complexity: O(n)
# Runtime: 36 ms (58.96%)
# Memory Usage: 14.4 MB (%)

solution0 = Solution()
print(solution0.heightChecker([1, 1, 4, 2, 1, 3]) == 3)
solution1 = Solution()
print(solution1.heightChecker([5, 1, 2, 3, 4]) == 5)
solution2 = Solution()
print(solution2.heightChecker([1, 2, 3, 4, 5]) == 0)
