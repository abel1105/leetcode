# Input: strs = ["flower","flow","flight"]
# Output: "fl"
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for index, text in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) < index + 1 or strs[j][index] != text:
                    return strs[0][0:index]
        return strs[0]

# Time complexity: O(S)
# Space Complexity: O(1)
# Runtime: 46 ms (20.71%)
# Memory Usage: 14.4 MB (55.41%)
