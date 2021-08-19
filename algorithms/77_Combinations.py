#
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.backtrack([], 1, n, k, [])

    def backtrack(self, c, i, n, k, r):
        if len(c) == k:
            r.append(list(c))
            return r

        for j in range(i, n + 1):
            if k - len(c) <= n + 1 - j:
                c.append(j)
                r = self.backtrack(c, j + 1, n, k, r)
                c.pop()

        return r

# https://stackoverflow.com/questions/31120402/complexity-when-generating-all-combinations
# Time complexity: O(n ^ min{k, n - k})
# Space Complexity: O(k)
# Runtime: 92 ms (84.59%)
# Memory Usage: 15.6 MB (92.68%)
