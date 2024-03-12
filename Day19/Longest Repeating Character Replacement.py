class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap={}

        l=0
        res=0
        #sliding window concept
        for r in range(len(s)):

            charmap[s[r]]=1+ charmap.get(s[r],0)

            while((r-l+1) -max(charmap.values()) > k ):

                
                charmap[s[l]] = charmap[s[l]]-1
                l=l+1
            
            res=max(res,r-l+1)
        return res

        

        
