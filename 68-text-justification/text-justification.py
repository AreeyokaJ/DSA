class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = [] 
        length, line = 0, []


        for word in words: 

            if len(line) + length + len(word) > maxWidth: 

                extra_space = maxWidth - (length + len(line) - 1)
                spaces = extra_space // max(1, len(line) - 1) 
                remainder = extra_space % max(1, len(line) - 1) 

                for i in range(max(len(line) - 1, 1)):
                    line[i] += " " * spaces
                    
                    if remainder:
                        line[i] += " " 
                        remainder -= 1 

                ans.append(" ".join(line))
                length = 0 
                line = [] 
            
            length += len(word) 
            line.append(word) 

        

        last_line = " ".join(line) 
        extra_space = maxWidth - len(last_line) 
        ans.append(last_line + " " * extra_space)
        return ans