class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if(i.isalnum()):
                res=res+i
        res=res.lower()

        print(res)
        i=0
        j=len(res)-1

        while(i<=j):
            if(res[i]!=res[j]):
                return False
            i=i+1
            j=j-1
        
        return True

    #     l,r=0,len(s)-1

    #     while(l<r):
    #         while l<r and not alphanum(s[l]):
    #             l=l+1
    #         while r>l and not alphanum(s[r]):
    #             r=r-1

    #         if(s[l].lower() != s[r].lower()):
    #             return False
            
    #         l =l+1
    #         r=r-1
    #     return True

    # def alphanum(self,c):
    #     return (ord('A') <= ord(c) <= ord('Z') or ord('a') <=ord(c)<=ord('z') or ord('1')<=ord(c)<=ord('9'))
        
