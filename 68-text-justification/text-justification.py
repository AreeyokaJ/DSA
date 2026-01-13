class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        line = [] 
        length = 0 
        ans = []

        for word in words:

            if len(line) + len(word) + length > maxWidth: 
                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1, len(line) - 1)
                remainder = extra_spaces % max(1, len(line) - 1) 

                for i in range(max(1, len(line) - 1)):
                    line[i] = line[i] + " " * spaces

                    if remainder: 
                        line[i] += " "
                        remainder -= 1
                

                ans.append("".join(line))    
                length = 0
                line = [] 

            
            line.append(word)
            length += len(word) 

        last_line = " ".join(line) 
        extra_spaces = maxWidth - len(last_line) 

        ans.append(last_line + " " * extra_spaces)

        return ans