class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []

        #the current line is stored in line, it's an array because we want to count # of words 
        #the 0 is the variable for the length of the line 
            #basically the count of the chars in each of the words 
        line, length = [], 0 

        i = 0 

        while i < len(words):
            #length + (len(line)) [# of words currently in line] + the len of extra word
            if length + (len(line)) + len(words[i]) > maxWidth:
                # line complete 

                #extra_space = width - length (num of chars)
                extra_space = maxWidth - length 

                #the max(len(line) - 1, 1) is in case the len(line) == 1 which would give div by 0 err
                spaces = extra_space // max(len(line) - 1, 1)

                #this is remainder left over 
                remainder = extra_space % max(1, len(line) - 1)

                #if len(line) == 1 this loop will not run [j = 0    range(0)] therefore we must do max
                for j in range(max(1, len(line) - 1)):

                    #pythonic way of adding x amount of spaces to a string 
                    line[j] += " " * spaces 

                    #this remainder clause will add space at the end of the first remainder words 
                    if remainder:
                        line[j] += " "
                        remainder -= 1 

                res.append("".join(line))

                #reset the line 
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            i += 1

        #handling the last line  
        last_line = " ".join(line) 
        trail_space = maxWidth - len(last_line) 
        res.append(last_line + " " * trail_space)
        
        
        return res