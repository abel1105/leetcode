# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

class Solution:
    def numSplits(self, s: str) -> int:
        right = {}
        left = {}
        count = 0

        for i in s:
            if i not in right:
                right[i] = 1
            else:
                right[i] += 1

        for i in s:
            if i not in left:
                left[i] = 1
            else:
                left[i] += 1

            right[i] -= 1
            if right[i] == 0:
                del right[i]

            if len(left) == len(right):
                count += 1

        return count


# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 188 ms (66.83%)
# Memory Usage: 15 MB (45.37%)
