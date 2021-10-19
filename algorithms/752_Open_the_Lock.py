# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        queue = deque(['0000'])
        steps = 0
        while queue:
            for i in range(len(queue)):
                candidate = queue.popleft()
                if candidate == target:
                    return steps
                if candidate in visited:
                    continue
                visited.add(candidate)
                queue.extend(self.getCandidates(candidate))
            steps += 1

        return -1

    def getCandidates(self, cur):
        result = []
        for i in range(4):
            result.append(cur[:i] + str((int(cur[i]) + 1) % 10) + cur[i + 1:])
            result.append(cur[:i] + str((int(cur[i]) - 1) % 10) + cur[i + 1:])
        return result

# Time complexity: O(4^2 * 10^4)
# Space Complexity: O(10^4)
# Runtime: 700 ms (59.05%)
# Memory Usage: 15.8 MB (17.59%)
