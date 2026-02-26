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

    def prune_words(self, word):

        parentNChild = [] 
        curr = self
        for c in word:
            parentNChild.append([curr, c])
            curr = curr.children[c] 

        for parent, childKey in reversed(parentNChild):

            child = parent.children[childKey] 

            if not child.children:
                del parent.children[childKey]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode() 
        
        for word in words:
            root.add_word(word) 
        
        rows = len(board)
        cols = len(board[0]) 

        ans = set()

        visit = set() 

        def dfs(r, c, prefix, node):
            if min(r, c) < 0 or r == rows or c == cols:
                return  

            if board[r][c] not in node.children or (r, c) in visit:
                return 


            visit.add((r, c))

            node = node.children[board[r][c]]
            prefix += board[r][c]
            if node.word:
                ans.add(prefix) 
                root.prune_words(prefix)

            dfs(r + 1, c, prefix, node)
            dfs(r - 1, c, prefix, node)
            dfs(r, c + 1, prefix, node)
            dfs(r, c - 1, prefix, node) 

            visit.remove((r,c)) 
            



        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root) 

        
        return list(ans)