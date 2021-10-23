# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]

        for index, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                old_index = stack.pop()
                result[old_index] = index - old_index

            stack.append(index)

        return result


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 1240 ms (72.89%)
# Memory Usage: 25.1 MB (71.43%)
