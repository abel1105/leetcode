# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)
        for val in nums:
            if len(self.heap) == self.k:
                heapq.heappushpop(self.heap, val)
            else:
                heapq.heappush(self.heap, val)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]

# Time complexity: O(NlogN)
# Space Complexity: O(N)
# Runtime: 117 ms (40.58%)
# Memory Usage: 18.4 MB (52.49%)
