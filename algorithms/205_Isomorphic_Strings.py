# Input: s = "egg", t = "add"
# Output: true
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_book = {}
        t_book = {}

        for i in range(len(s)):
            if s[i] in s_book:
                if t[i] != s_book[s[i]]:
                    return False
            elif t[i] in t_book:
                if s[i] != t_book[t[i]]:
                    return False
            else:
                s_book[s[i]] = t[i]
                t_book[t[i]] = s[i]

        return True


# Time complexity: O(N)
# Space Complexity: O(1) ASCII
# Runtime: 32 ms (96.78%)
# Memory Usage: 14.5 MB (24.69%)
