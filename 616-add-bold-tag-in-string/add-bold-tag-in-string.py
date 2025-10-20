class TrieNode: 
    def __init__(self):
        self.children = {}
        self.word = False


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s) 

        #build Trie
        root = TrieNode() 

        for word in words: 
            curr = root 

            for c in word: 
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                
                curr = curr.children[c] 
            
            curr.word =True

        
        for i in range(len(s)):
            j = i 

            longest = -1 
            curr = root
            while j < len(s) and s[j] in curr.children:
                curr = curr.children[s[j]]

                if curr.word:
                    longest = j 
                
                j += 1 

            if longest != -1:
                for k in range(i, longest + 1):
                    bold[k] = True 

        # for word in words:
        #     start = s.find(word)
        #     length = len(word) 

        #     while start != -1:
        #         for i in range(start, start + length):
        #             bold[i] = True 

        #         start = s.find(word, start + 1) 

        
        ans = [] 

        i = 0 

        while i < len(s):
            if bold[i]:
                ans.append("<b>")

                while i < len(s) and bold[i]:
                    ans.append(s[i]) 
                    i += 1 

                ans.append("</b>")
            else:
                ans.append(s[i])
                i += 1

        return "".join(ans)