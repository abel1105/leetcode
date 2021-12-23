# Input: m = 3, n = 7
# Output: 28
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            for i in range(n):
                if i > 0:
                    row[i] += row[i - 1]

        return row[-1]

# Time complexity: O(mn)
# Space Complexity: O(n)
# Runtime: 32 ms (63.94%)
# Memory Usage: 14.3MB (38.39%)
