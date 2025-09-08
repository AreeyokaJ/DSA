class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        ans = []
        for i in range(n):
            if self.contains_zero(i) or self.contains_zero(n - i):
                continue 

            ans.append(i) 
            ans.append(n - i)
            break
        return ans

    def contains_zero(self, s): 
        s = str(s)

        for c in s:
            if c == "0":
                return True 
        
        return False 