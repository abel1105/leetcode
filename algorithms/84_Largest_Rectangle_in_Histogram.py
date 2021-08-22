# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []  # (index, height)
        start = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                result = max(result, area)
                start = index
            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            result = max(result, area)

        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 796 ms (63.52%)
# Memory Usage: 30.8M B (7.90%)
