# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1

        if right < 1:
            return A

        while left < right:
            if A[left] % 2 != 0 and A[right] % 2 == 0:
                temp = A[right]
                A[right] = A[left]
                A[left] = temp
                left += 1
                right -= 1
            elif A[left] % 2 == 0 and A[right] % 2 != 0:
                left += 1
                right -= 1
            elif A[left] % 2 == 0:
                left += 1
            elif A[right] % 2 != 0:
                right -= 1
        return A


# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 76 ms (80.62%)
# Memory Usage: 15.1 MB (55.47%)

solution0 = Solution()
print(solution0.sortArrayByParity([3, 1, 2, 4]))
