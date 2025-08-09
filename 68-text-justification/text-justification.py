class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        line,length = [], 0 

        res = []

        for i in range(len(words)):

            if len(line) + len(words[i]) + length > maxWidth:

                extra_space = maxWidth - length 
                spaces = extra_space // max((len(line) - 1), 1)
                remainder = extra_space % max(len(line) - 1, 1) 

                for j in range(max(len(line) - 1, 1)): 
                    line[j] += " " * spaces 
                    if remainder:
                        line[j] += " " 
                        remainder -= 1
                
                res.append("".join(line))
                line = []
                length = 0

            line.append(words[i])
            length += len(words[i])

        last_line = " ".join(line)
        extra_space = maxWidth -len(last_line)
        
        res.append(last_line + " " * extra_space)

        return res
        

