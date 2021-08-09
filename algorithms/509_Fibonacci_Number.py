# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.


class Solution:
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1
        }

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        result = self.fib(n - 1) + self.fib(n - 2)

        if not n in self.cache:
            self.cache[n] = result
        return result

# Time complexity: O(n)
# Space Complexity: O(n)
# Runtime: 32 ms (61.74%)
# Memory Usage: 14.2 MB (41.63%)
