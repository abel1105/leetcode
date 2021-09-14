# Input: haystack = "hello", needle = "ll"
# Output: 2

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        text = list(haystack)
        pattern = list(needle)
        prefix = self.buildPrefixTable(pattern)
        i, j = 0, 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = prefix[j - 1]
                else:
                    i += 1

            if j > len(pattern) - 1:
                return i - j
        return -1

    def buildPrefixTable(self, pattern):
        prefix = [0] * len(pattern)
        i, j = 0, 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                prefix[j] = i + 1
                i += 1
                j += 1
            else:
                if i > 0:
                    i = prefix[i - 1]
                else:
                    prefix[j] = 0
                    j += 1
        return prefix


# Time complexity: O(m+n)
# Space Complexity: O(n)
# Runtime: 128ms (13.09%)
# Memory Usage: 15.9MB (%)
