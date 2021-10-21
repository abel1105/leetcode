# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
from collections import deque
import math


class Solution:
    def numSquares(self, n: int) -> int:
        steps = 0
        queue = deque([n])
        visited = set()
        options = self.getOptions(n)
        while queue:
            steps += 1
            for i in range(len(queue)):
                val = queue.popleft()
                for i in options:
                    if val - i == 0:
                        return steps
                    elif (val - i) in visited:
                        continue
                    elif val - i > 0:
                        visited.add(val - i)
                        queue.append(val - i)

    def getOptions(self, val):
        result = []
        for i in range(int(math.sqrt(val)), 0, -1):
            result.append(i ** 2)

        return result

# Time complexity: O(N^2)
# Space Complexity: O(N^2)
# Runtime: 236 ms (80.78%)
# Memory Usage: 15.2 MB (27.74%)
