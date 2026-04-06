class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if "0" in [num1, num2]:
            return "0"

        ans = [0] * (len(num1) + len(num2)) 

        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j]) 

                ans[i + j] += digit 
                ans[i + j + 1] += (ans[i+j] // 10)
                ans[i + j] %= 10 

        
        ans = ans[::-1] 

        beg = 0

        while beg < len(ans) and ans[beg] == 0:
            beg += 1 
        
        ans = ans[beg:]
        res = []

        for num in ans:
            res.append(str(num))

        
        return ("".join(res))