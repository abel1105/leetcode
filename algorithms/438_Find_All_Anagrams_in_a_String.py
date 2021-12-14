# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        hashMap = {}

        for i in p:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        count = len(hashMap)

        start = 0
        end = 0
        while end < len(s):

            if s[end] in hashMap:
                hashMap[s[end]] -= 1
                if hashMap[s[end]] == 0:
                    count -= 1

            end += 1

            if count == 0:
                result.append(start)

            if end - start == len(p):
                if s[start] in hashMap:
                    if hashMap[s[start]] == 0:
                        count += 1
                    hashMap[s[start]] += 1
                start += 1

        return result

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 165 ms (41.89%)
# Memory Usage: 15 MB (93.41%)
