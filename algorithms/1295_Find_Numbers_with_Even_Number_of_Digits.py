# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count


# Time Complexity: O(n)
# Space Complexity: O(1)
# Runtime: 52 ms (72.66%)
# Memory Usage: 14.1 MB (89.55%)

solution0 = Solution()
print(solution0.findNumbers([12, 345, 2, 6, 7896]) == 2)
solution1 = Solution()
print(solution1.findNumbers([555, 901, 482, 1771]) == 1)
