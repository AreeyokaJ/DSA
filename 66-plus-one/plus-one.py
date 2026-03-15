class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    


        n = len(digits) 

        for i in range(n-1, -1, -1):
            carry = 1

            if digits[i] + carry == 10:
                carry = 1 
                digits[i] = 0 

            else: 
                digits[i] += 1 
                carry = 0 
                break
            
        if carry:
            digits = [1] + digits

        return digits