# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
from typing import List

from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        queue = deque([])

        for i in range(len(graph[0])):
            queue.append(([0], graph[0][i]))

        while queue:
            (temp, index) = queue.popleft()
            if index == len(graph) - 1:
                temp.append(index)
                ans.append(list(temp))
            else:
                temp.append(index)
                for i in range(len(graph[index])):
                    queue.append((list(temp), graph[index][i]))

        return ans

# Time complexity: O(N * 2 ^ N)
# Space Complexity: O(N * 2 ^ N)
# Runtime: 100 ms (70.86%)
# Memory Usage: 15.8 MB (20.83%)
