# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = {}
        result = 0
        start = 0
        for key, i in enumerate(s):
            if i not in bucket:
                bucket[i] = key
            else:
                if start < bucket[i] + 1:
                    start = bucket[i] + 1
                bucket[i] = key
            result = max(result, key - start + 1)
        return result


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 48 ms (97.17%)
# Memory Usage: 14.4 MB (53.71%)
