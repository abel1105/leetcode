# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation:
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1

        for index in range(len(arr) - 1, -1, -1):
            temp = arr[index]

            arr[index] = max

            max = max if max > temp else temp

        return arr


# Time complexity: O(n)
# Space Complexity: O(1)
# Runtime: 116 ms (91.00%)
# Memory Usage: 15.5 MB (25.93%)

solution0 = Solution()
print(solution0.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1])
solution1 = Solution()
print(solution1.replaceElements([400]) == [-1])
