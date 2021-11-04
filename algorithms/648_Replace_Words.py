# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            cur = root
            for char in word:
                cur = cur.children.setdefault(char, TrieNode())
            cur.isEnd = True

        words = sentence.split()

        for key, word in enumerate(words):
            cur = root
            index = 0
            for char in word:
                if char not in cur.children:
                    break
                index += 1
                cur = cur.children[char]
                if cur.isEnd:
                    break
            if cur is not root and cur.isEnd:
                words[key] = words[key][:index]

        return ' '.join(words)

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 116 ms (72.72%)
# Memory Usage: 35.7 MB (30.29%)
