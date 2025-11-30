class TrieNode():
    def __init__(self):
        self.children = {} 
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c] 

        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j, node):

            curr = node
            for i in range(j, len(word)):
                c = word[i] 

                if c == ".":
                    for n in curr.children.values():
                        if dfs(i + 1, n): return True 

                    return False 

                else:
                    if c in curr.children:
                        curr = curr.children[c] 
                    else:
                        return False 
            
            return curr.word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)