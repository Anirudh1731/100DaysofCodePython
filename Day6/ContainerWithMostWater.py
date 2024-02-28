class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1

        while(l<r):

            area=(r-l)*min(height[l],height[r])
            res=max(area,res)

            if height[l] < height[r]:
                l=l+1
            elif height[l] > height[r]:
                r=r-1
            else:
                r=r-1
        return res


        
