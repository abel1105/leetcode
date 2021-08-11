# Input: n = 3, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2:
            return 0 if self.kthGrammar(n - 1, (k + 1) / 2) == 0 else 1
        else:
            return 1 if self.kthGrammar(n - 1, k / 2) == 0 else 0

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 32 ms (52.54%)
# Memory Usage: 14.2 MB (80.74%)
