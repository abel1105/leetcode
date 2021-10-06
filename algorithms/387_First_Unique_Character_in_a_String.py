# Input: s = "leetcode"
# Output: 0

class Solution:
    def firstUniqChar(self, s: str) -> int:
        bucket = {}
        for i in s:
            if i in bucket:
                bucket[i] += 1
            else:
                bucket[i] = 1

        for key, i in enumerate(s):
            if bucket[i] == 1:
                return key

        return -1


# Time complexity: O(N)
# Space Complexity: O(1) ASCII
# Runtime: 179 ms (28.11%)
# Memory Usage: 14.5 MB (43.99%)
