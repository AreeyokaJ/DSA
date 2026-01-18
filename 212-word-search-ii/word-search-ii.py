class TrieNode():
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

    def prune_word(self, word): 
        parent_child = [] 
        curr = self 
        for c in word:
            parent_child.append([curr, c])
            curr = curr.children[c] 

    
        for parent, childkey in reversed(parent_child):
            childNode = parent.children[childkey] 

            if not childNode.children: 
                del parent.children[childkey] 
            
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode() 

        for w in words:
            root.add_word(w) 

        rows = len(board) 
        cols = len(board[0])

        visit = set() 
        ans = set()

        def dfs(r, c, prefix, node):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit: 
                return 

            if board[r][c] not in node.children:
                return 


            visit.add((r, c)) 

            prefix += board[r][c] 
            node = node.children[board[r][c]] 
            
            if node.word:
                ans.add(prefix) 
                root.prune_word(prefix)

            dfs(r + 1, c, prefix, node)
            dfs(r - 1 , c, prefix, node)
            dfs(r, c + 1, prefix, node)
            dfs(r, c - 1, prefix, node)

            visit.remove((r, c)) 


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root)

    
        return list(ans)