class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1
        res=nums[0]
        while(l<=r):
            if(nums[l]<nums[r]):
                res=min(nums[l],res)
                break

            mid=(l+r)//2
            res=min(nums[mid],res)
            if(nums[mid]>=nums[l]):
                l=mid+1
            elif(nums[mid]<nums[l]):
                r=mid-1
        return res






        
