class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        line, length = [], 0 
        ans = []
        for word in words:
            if length + len(word) + len(line) > maxWidth: 
                extra_space = maxWidth - (length)
                spaces = extra_space // max((len(line) - 1), 1)
                     
                remainder = extra_space % max((len(line) - 1), 1) 
                for i in range(max(1, len(line) - 1)): 
                    line[i] += " " * spaces 
                    
                    if remainder:
                        line[i] += " "
                        remainder -= 1 

                ans.append("".join(line))
                line = [] 
                length = 0
            
            line.append(word)
            length += len(word) 
        
        last_line = " ".join(line) 
        extra_space = maxWidth - len(last_line)
        ans.append(last_line + " " * extra_space)
        
        return ans

