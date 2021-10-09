# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in bucket:
                bucket[key].append(i)
            else:
                bucket[key] = [i]

        result = []
        for i in bucket:
            result.append(bucket[i])

        return result

# Time complexity: O(N* MlogM) M = len of str
# Space Complexity: O(N * N)
# Runtime: 92 ms (93.25%)
# Memory Usage: 16.9 MB (98.41%)
