# Input: x = 2.00000, n = 10
# Output: 1024.00000


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = abs(n)

        def helper(x: float, n: int, r: float):
            if n == 0:
                return r
            if n % 2:
                return helper(x, n - 1, r * x)
            else:
                return helper(x * x, n / 2, r)

        return helper(x, n, 1)

# Time complexity: O(logN)
# Space Complexity: O(logN)
# Runtime: 32 ms (58.65%)
# Memory Usage: 14.1 MB (79.19%)
