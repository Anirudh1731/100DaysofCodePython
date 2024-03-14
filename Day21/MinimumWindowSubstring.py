class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if(t==""):
            return ""
        # 2 hashmaps 1 for window and 1 for string 
        h1,h2={},{}

      #matching hahsmap created
        for c in t:
            h1[c]=1+h1.get(c,0)
        
        have,need=0,len(h1)

        l=0
        res,resLength=[-1,-1],float("infinity")

      #iterating in the window
        for r in range(len(s)):
            c=s[r]

            h2[c]=1+h2.get(c,0)
            
            # if it matches the incrementing have
            if c in h1 and h2[c] == h1[c]:
                have+=1

            # if have is same then we start shrinking our window
            while (have==need):

                if(r-l+1 < resLength):
                    res=[l,r]
                    resLength=r-l+1
                
                h2[s[l]]-=1
                # if the removed element is making the match unequal then we reduce
                if s[l] in h1 and h2[s[l]]<h1[s[l]]:
                    have-=1
                
                l=l+1
        l,r=res

        if resLength!=float("infinity"):
            return s[l:r+1]
        else:
            return ""
            

            
        
