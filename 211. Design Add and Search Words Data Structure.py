class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word, 0)
        return self.res

    def dfs(self, node, word, i):
        if i >= len(word):
            if node.is_word:
                self.res = True
            return
        if word[i] == '.':
            for n in node.children.values():
                self.dfs(n, word, i + 1)
        else:
            node = node.children.get(word[i])
            if not node:
                return
            self.dfs(node, word, i + 1)
