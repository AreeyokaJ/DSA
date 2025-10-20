class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False] * len(s)


        for word in words:
            start = s.find(word) 
            length = len(word) 

            while start != -1:
                for i in range(start, start + length):
                    bold[i] = True 

                start = s.find(word, start + 1) 

        
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