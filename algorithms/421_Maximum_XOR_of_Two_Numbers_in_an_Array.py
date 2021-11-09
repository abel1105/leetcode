# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        for num in nums:
            cur = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1  # get ith bit
                if bit not in cur.children:
                    cur.children[bit] = TrieNode()
                cur = cur.children[bit]
        curMax = 0
        for num in nums:
            cur = root
            curSum = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1  # get ith bit
                opposite = 1 ^ bit
                if opposite in cur.children:
                    curSum += 1 << i
                    cur = cur.children[opposite]
                else:
                    cur = cur.children[bit]
            curMax = max(curMax, curSum)

        return curMax

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 5792 ms (21.22%)
# Memory Usage: 145.3 MB (19.58%)
