# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        num1 = len(s) - 1
        num2 = len(t) - 1

        while 0 <= num1 or 0 <= num2:
            char1 = char2 = ''
            if num1 >= 0:
                num1, char1 = self.getChar(s, num1)
            if num2 >= 0:
                num2, char2 = self.getChar(t, num2)

            if char1 != char2:
                return False

        return True

    def getChar(self, text, num):
        count = 0
        char = ''
        while num >= 0 and (count > 0 or char == ''):
            if text[num] == '#':
                count += 1
            elif count > 0:
                count -= 1
            else:
                char = text[num]
            num -= 1

        return num, char

# Time complexity: O(N)
# Space Complexity: O(1)
# Runtime: 28 ms (86.65%)
# Memory Usage: 14.3 MB (0%)
