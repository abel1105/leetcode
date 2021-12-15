# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        result = 0
        for i in range(len(isConnected)):
            if i not in seen:
                result += 1
                self.check(isConnected, i, seen)
        return result

    def check(self, isConnected, n, seen):
        for i, v in enumerate(isConnected[n]):
            if v == 1 and i not in seen:
                seen.add(i)
                self.check(isConnected, i, seen)

# Time complexity: O(N)
# Space Complexity: O(L)
# Runtime: 209 ms (42.29%)
# Memory Usage: 14.8 MB (51.68%)
