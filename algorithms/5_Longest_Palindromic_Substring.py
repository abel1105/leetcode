# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

class Solution:
    start = 0
    max = 0

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2: return s
        for i in range(0, l):
            if l - i < self.max / 2:
                break
            self.extendPalindrome(s, i, i)
            self.extendPalindrome(s, i, i + 1)

        return s[self.start:(self.start + self.max)]

    def extendPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if self.max < (right - left - 1):
            self.start = left + 1
            self.max = right - left - 1

# Time complexity: O(n^2)
# Space Complexity: O(1)
# Runtime: 560 ms (91.70%)
# Memory Usage: 14.4 MB (60.46%)
