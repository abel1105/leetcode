# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

class Solution:
    def decodeString(self, s: str) -> str:
        repeat = 0
        cur = ''
        stacks = []

        for i in s:
            if i.isdigit():
                repeat = repeat * 10 + int(i)
            elif i == '[':
                stacks.append(cur)
                stacks.append(repeat)
                cur = ''
                repeat = 0
            elif i == ']':
                repeat = stacks.pop()
                prev = stacks.pop()
                cur = prev + cur * repeat
                repeat = 0
            else:
                cur += i

        return cur

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 20 ms (99.40%)
# Memory Usage: 14 MB (92.99%)
