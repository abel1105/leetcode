# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for i in word:
            if i not in t:
                t[i] = {}
            t = t[i]
        t['#'] = 1

    def search(self, word: str) -> bool:
        t = self.trie
        for i in word:
            if i not in t:
                return False
            t = t[i]

        return '#' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for i in prefix:
            if i not in t:
                return False
            t = t[i]
        return True

# Time complexity: O(N)
# Space Complexity: O(N)
# Runtime: 116 ms (99.35%)
# Memory Usage: 27.7 MB (89.25%)
