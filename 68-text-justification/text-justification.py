class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        line = [] 
        length = 0 
        ans = []


        for word in words:
            if len(word) + length + len(line) > maxWidth:
                extra_spaces = maxWidth - length 
                spaces = extra_spaces // max(1, len(line) - 1)
                remainder = extra_spaces % max(1, len(line) - 1)

                for i in range(max(1, len(line) - 1)):
                    line[i] += " " * spaces

                    if remainder:
                        remainder -= 1
                        line[i] += " " 
                
                ans.append("".join(line))
                length = 0 
                line = []
            
            line.append(word)
            length += len(word)

        last_line = " ".join(line) 

        extra_spaces = maxWidth - len(last_line)

        last_line += (" " * extra_spaces)
        ans.append(last_line)
        return ans