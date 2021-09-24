# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        self.reverse(s, 0, n - 1)
        self.reverseWord(s)
        return ''.join(self.cleanSpace(s))

    def reverseWord(self, s):
        n = len(s)
        i = j = 0
        while j < n:
            while i < j or (i < n and s[i] == ' '):
                i += 1
            while j < i or (j < n and s[j] != ' '):
                j += 1
            self.reverse(s, i, j - 1)

    def cleanSpace(self, s):
        n = len(s)
        i = j = 0
        while j < n:
            while j < n and s[j] == ' ':
                j += 1
            while j < n and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1
            while j < n and s[j] == ' ':
                j += 1
            if j < n:
                s[i] = ' '
                i += 1

        return s[0:i]

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28 ms (12.29%)
# Memory Usage: 14.2 MB (%)
