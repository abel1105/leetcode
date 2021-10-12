# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        bucket = set(jewels)
        result = 0
        for i in stones:
            if i in bucket:
                result += 1

        return result

# Time complexity: O(j + s)
# Space Complexity: O(j)
# Runtime: 24 ms (96.58%)
# Memory Usage: 14.2 MB (72.44%)
