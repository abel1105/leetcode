# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            return word == word[::-1]

        result = []
        bucket = {word: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                suf = word[:j]
                pre = word[j:]
                if isPalindrome(suf):
                    back = pre[::-1]
                    if back != word and back in bucket:
                        result.append([bucket[back], i])
                if n != j and isPalindrome(pre):
                    back = suf[::-1]
                    if back != word and back in bucket:
                        result.append([i, bucket[back]])

        return result

# Time complexity: O(n * W ^2) w = average word length
# Space Complexity: O(n)
# Runtime: 1416 ms (81.85%)
# Memory Usage: 21.9 MB (50.81%)
