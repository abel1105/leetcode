# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = word

        result = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtrack(board, root, i, j, result)

        return result

    def backtrack(self, board, trie, row, column, result):
        char = board[row][column]
        if char not in trie.children:
            return
        trie = trie.children[char]
        if trie.word:
            result.append(trie.word)
            trie.word = None

        board[row][column] = '#'

        for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r = row + i
            c = column + j
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                self.backtrack(board, trie, r, c, result)

        board[row][column] = char

# Time complexity: O(M*N)
# Space Complexity: O(M*N)
# Runtime: 8952 ms (13.60%)
# Memory Usage: 16.4 MB (7.3%)
