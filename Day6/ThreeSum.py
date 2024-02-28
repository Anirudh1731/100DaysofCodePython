class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums.sort()

        for i,e in enumerate(nums):
            if(i>0 and e==nums[i-1]):
                continue
            
            l,r=i+1,len(nums)-1

            while(l<r):
                if(nums[l]+nums[r]+e==0):
                    res.append([nums[l],nums[r],e])
                    l=l+1
                    while(l<r and nums[l]==nums[l-1]):
                        l=l+1
                elif(nums[l]+nums[r]+e < 0):
                    l=l+1
                else:
                    r=r-1
        return res
        
