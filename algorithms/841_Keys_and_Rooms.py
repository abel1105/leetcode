# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation:
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()

        while queue:
            key = queue.popleft()
            if key not in visited:
                visited.add(key)
                queue.extend(rooms[key])

        return len(visited) == len(rooms)

# Time complexity: O(N + E)
# Space Complexity: O(N)
# Runtime: 56 ms (98.51%)
# Memory Usage: 14.6 MB (94.45%)
