# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        first = 1
        second = 2

        for _ in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 20 ms (98.96%)
# Memory Usage: 14.1 MB (90.70%)
