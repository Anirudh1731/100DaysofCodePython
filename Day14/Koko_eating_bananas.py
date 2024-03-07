class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r=1,max(piles)

        result=r

        while(l<=r):
            mid=(l+r)//2

            hours=0
            for p in piles:
                hours+= math.ceil(p/mid)

            if(hours<=h):
                result=min(result,mid)
                r=mid-1
            else:
                l=mid+1

        return result

        
