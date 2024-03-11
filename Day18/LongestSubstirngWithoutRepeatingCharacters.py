class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        charset=set()
        res=0
        
        #sliding window
        for j in range(len(s)):

            while(s[j] in charset):
                charset.remove(s[l])
                l=l+1
            charset.add(s[j])
            res=max(res,j-l+1)
        return res





            

        
