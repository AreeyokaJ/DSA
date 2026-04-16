class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        index = -1
        for i in range(len(strs[0])):
            curr = strs[0][i]
            for s in strs:
                if i > len(s) - 1 or s[i] != curr:
                    return strs[0][:i]
            index = i  + 1

        return strs[0][:index]

        
        