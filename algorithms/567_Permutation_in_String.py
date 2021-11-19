# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        collect = [0] * 26
        for i in s1:
            collect[self.getIndex(i)] += 1

        start, end, count = 0, 0, len(s1)
        while end < len(s2):
            if collect[self.getIndex(s2[end])] > 0:
                count -= 1
            collect[self.getIndex(s2[end])] -= 1

            end += 1

            if count == 0:
                return True
            if end - start == len(s1):
                if collect[self.getIndex(s2[start])] >= 0:
                    count += 1
                collect[self.getIndex(s2[start])] += 1
                start += 1

        return False

    def getIndex(self, s):
        return ord(s) - ord('a')

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 116 ms (44.69%)
# Memory Usage: 14.5 MB (35.26%)
