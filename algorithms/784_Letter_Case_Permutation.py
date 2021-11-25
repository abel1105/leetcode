# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, 0, [], result)

        return result

    def backtrack(self, s, start, cur, result):
        if len(cur) == len(s):
            result.append(''.join(cur))
            return

        if s[start].isnumeric():
            cur.append(s[start])
            self.backtrack(s, start + 1, cur, result)
            cur.pop()
        else:
            for j in [s[start].lower(), s[start].upper()]:
                cur.append(j)
                self.backtrack(s, start + 1, cur, result)
                cur.pop()

# Time complexity: O(2^N)
# Space Complexity: O(2^N)
# Runtime: 52 ms (87.26%)
# Memory Usage: 14.9 MB (61.45%)
