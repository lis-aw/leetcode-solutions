class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode=""
        for string in strs:
            count=len(string)
            encode+=f"{count}#{string}"   
        return encode
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result=[]
        i=0
        while i < len(s):
            j=i
            while s[j] is not '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+length+1])
            i=length+j+1
        return result




      
            

            



        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))