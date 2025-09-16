class TrieNode:
    def __init__(self):
        self.children = {} 
        self.word = False 

    def add_word(self, word):
        curr = self 

        for c in word: 
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c] 

        curr.word = True 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode() 

        for word in words:
            root.add_word(word) 
        
        rows = len(board) 
        cols = len(board[0]) 
        visit = set()
        ans = set()

        def dfs(r, c, word, node):
            #in bounds 
            if min(r, c) < 0 or r == rows or c == cols:
                return 
            
            if (r, c) in visit or board[r][c] not in node.children:
                return 

            visit.add((r, c))
            word += board[r][c] 
            node = node.children[board[r][c]]
            if node.word == True:
                ans.add(word) 
            
            dfs(r + 1, c, word, node) 
            dfs(r - 1, c, word, node) 
            dfs(r, c + 1, word, node) 
            dfs(r, c - 1, word, node) 

            visit.remove((r, c)) 
    

        for r in range(rows):
            for c in range(cols): 
                dfs(r, c, "", root)

        return list(ans)