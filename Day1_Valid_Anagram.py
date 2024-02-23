class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map1={}
        map2={}
        # approach1
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            map1[s[i]]=1+map1.get(s[i],0)
            map2[t[i]]=1+map2.get(t[i],0)

        for c in map1:
            if(map1[c] !=map2.get(c,0)):
                return False
            
            
        return True

        #approach 2
        # return sorted(s)==sorted(t)
