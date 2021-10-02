# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        bucket = set()
        while True:
            if n in bucket:
                return False
            bucket.add(n)
            result = 0
            for i in str(n):
                result += int(i) ** 2

            if result == 1:
                return True
            else:
                n = result

# Time complexity: O(logN)
# Space Complexity: O(logN)
# Runtime: 44 ms (27.86%)
# Memory Usage: 14.2 MB (47.61%)
