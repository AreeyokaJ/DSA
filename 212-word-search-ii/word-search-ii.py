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
    
    def removeWord(self, word) -> None:
        curr = self
        nodeAndChildKey = [] 

        for c in word:
            nodeAndChildKey.append([curr, c])
            curr = curr.children[c] 

        for parentNode, childKey in reversed(nodeAndChildKey): 
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
                break
            else: return 
        
        # nodeAndChildKey, = []
        # for char in word:
        #     nodeAndChildKey.append((cur, char))
        #     cur = cur.children[char]

        # for parentNode, childKey in reversed(nodeAndChildKey):
        #     targetNode = parentNode.children[childKey]
        #     if len(targetNode.children) == 0:
        #         del parentNode.children[childKey]
        #     else:
        #         return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            root.add_word(word) 
        


        ans = set()

        visit = set()
        rows = len(board)
        cols = len(board[0])


        def dfs(r, c, word, node):

            if (min(r, c) < 0 or r == rows or
                c == cols or (r, c) in visit):
                return 
            
            if board[r][c] not in node.children:
                return 
            visit.add((r, c))
           

            word += board[r][c]
            node = node.children[board[r][c]]
            if node.word:
                ans.add(word)
                root.removeWord(word)
                

            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node) 

            visit.remove((r,c))

        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "", root)

        return list(ans)




            