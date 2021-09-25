# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = j = 0
        while j < n:
            while i < j or (i < n and s[i] == ' '):
                i += 1
            while j < i or (j < n and s[j] != ' '):
                j += 1
            self.reverse(s, i, j - 1)

        return ''.join(s)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 128 ms (7.95%)
# Memory Usage: 15 MB (45.18%)
