# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i:j + 1] in wordDict:
                        dp[j + 1] = True

        return dp[-1]

# Time complexity: O(s^2 * k)
# Space Complexity: O(s)
# Runtime: 40 ms (58.92%)
# Memory Usage: 14.5 MB (47.81%)
