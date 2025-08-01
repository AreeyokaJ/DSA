class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [] 


        # i = 2 
        
        # c = 1 
        # for c in range(1, 1):
        #     group.append(ans[])
        
        for i in range(numRows): 
            if i == 0:
                ans.append([1])
            elif i == 1:
                ans.append([1, 1])

            else: 
                group = [1, ]
                prev = ans[i - 1]
                for c in range(len(prev) - 1):
                    group.append(prev[c] + prev[c + 1])

                group.append(1)
                ans.append(group)

        return ans


            
            

