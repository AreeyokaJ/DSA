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

    def pruneWord(self, word):
        
        parentChild = [] 

        curr = self

        for c in word: 
            parentChild.append([curr, c])
            curr = curr.children[c]
            
            
        
        for parentNode, child in reversed(parentChild):
            
            childNode = parentNode.children[child] 

            if not childNode.children:
                del parentNode.children[child]




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode() 
        
        for w in words:
            root.addWord(w) 

        rows = len(board) 
        cols = len(board[0])

        visit = set()
        ans = set()
        def dfs(r, c, node, pref):
            if (min(r, c) < 0 or r == rows or c == cols or 
                board[r][c] not in node.children or (r, c) in visit
            ):
                return 

            pref += board[r][c]

            node = node.children[board[r][c]]
            if node.word:
                ans.add(pref) 
                root.pruneWord(pref)

            visit.add((r, c))
            dfs(r + 1, c, node, pref)
            dfs(r - 1, c, node, pref)
            dfs(r, c + 1, node, pref)
            dfs(r, c - 1, node, pref) 
            visit.remove((r,c))
            return



        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        

        return list(ans)