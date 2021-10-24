# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = '+-*/'

        def evaluate(i):
            last = stack.pop()
            first = stack.pop()
            if i == '+':
                return first + last
            elif i == '-':
                return first - last
            elif i == '*':
                return first * last
            elif i == '/':
                return math.trunc(first / last)

        for i in tokens:
            if i in ops:
                stack.append(evaluate(i))
            else:
                stack.append(int(i))

        return stack[0]

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 70 ms (58.73%)
# Memory Usage: 14.7 MB (45.89%)
