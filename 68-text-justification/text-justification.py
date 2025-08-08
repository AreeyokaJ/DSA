class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = [] 

        line, length = [], 0 

        i = 0 

        while i < len(words):

            if len(line) + len(words[i]) + length> maxWidth: 
                #line complete 

                #extra_space 
                extra_space = maxWidth - length

                #spaces  
                spaces = extra_space // max(1, len(line) - 1) 

                #remainder 
                remainder = extra_space % max(1, len(line) - 1) 

                for j in range(max(1, len(line) - 1)): 
                    line[j] += " " * spaces 
                  
                    if remainder: 
                        line[j] += " " 
                        remainder -= 1 

                res.append("".join(line))
        
                #reset line 
                line = [] 
                length = 0 
            

            line.append(words[i])
            length += len(words[i])
            i += 1
    
        #handle last line 
        #last_line = " ".join(line)
        #trailing = maxWidth - len(last_line) 
        #res.append(last_line + " "  * trailing)

        extra_spaces = maxWidth - length - (len(line) - 1)  
        res.append(" ".join(line) + " " * extra_spaces)
        return res



