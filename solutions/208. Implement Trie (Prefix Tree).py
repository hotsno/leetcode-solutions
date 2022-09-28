class Trie:
    class Node:
        def __init__(self):
            self.next_level = [None] * 26
            self.ends_here = False

    def __init__(self):
        self.node = self.Node()  

    def insert(self, word: str) -> None:
        cur = self.node
        for c in word:
            ci = ord(c) - ord('a')
            if not cur.next_level[ci]:
                cur.next_level[ci] = self.Node()
            cur = cur.next_level[ci]
        cur.ends_here = True

    def search(self, word: str) -> bool:
        cur = self.node
        for c in word:
            ci = ord(c) - ord('a')
            if not cur.next_level[ci]:
                return False
            cur = cur.next_level[ci]
        return cur.ends_here
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for c in prefix:
            ci = ord(c) - ord('a')
            if not cur.next_level[ci]:
                return False
            cur = cur.next_level[ci]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

