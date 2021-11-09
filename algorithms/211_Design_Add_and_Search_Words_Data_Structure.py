# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children.setdefault(char, TrieNode())
        cur.isEnd = True

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, index, word, node):
        if index == len(word):
            return node.isEnd
        char = word[index]
        if char == '.':
            for key in node.children:
                if self.dfs(index + 1, word, node.children[key]):
                    return True
            return False
        elif char not in node.children:
            return False
        return self.dfs(index + 1, word, node.children[char])

# Time complexity: O(N^2)
# Space Complexity: O(N)
# Runtime: 372 ms (42.25%)
# Memory Usage: 29 MB (39.55%)
