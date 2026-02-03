class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string = []

        for s in strs:
            string.append(str(len(s)) + "#" + s)

        return "".join(string)
       
    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        i = 0 
       
        ans = []
        while i < len(s):
            j = i 
            while j < len(s) and s[j] != "#":
                j += 1 

            length = int(s[i:j])

            ans.append(s[j + 1:j + length + 1])

            i = j + 1 + length 

        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))