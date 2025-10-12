class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        curr = self 

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c] 
        
        curr.word = True
    
    def removeWord(self, word):
        parentAndChildKey = []
        curr = self 
        for c in word:
            parentAndChildKey.append([curr, c])
            curr = curr.children[c] 

        for parent, childKey in reversed(parentAndChildKey):
            if not parent.children[childKey].children:
                del parent.children[childKey]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #add words to Trie 
        root = TrieNode() 
        
        for word in words:
            root.addWord(word)

        rows = len(board)
        cols = len(board[0]) 

        visit = set()
        res = set()

        def dfs(r, c, node, prefix):
            if (min(r, c) < 0 or r == rows or c == cols or 
                 board[r][c] not in node.children or (r, c) in visit):
                return 
            
            visit.add((r, c))
            char = board[r][c]

            node = node.children[char]
            prefix += char
            if node.word == True:
                res.add(prefix)
                root.removeWord(prefix) 

            dfs(r + 1, c, node, prefix)
            dfs(r - 1, c, node, prefix)
            dfs(r, c + 1, node, prefix)
            dfs(r, c - 1, node, prefix)
            visit.remove((r,c))
            return 

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")


        return list(res)