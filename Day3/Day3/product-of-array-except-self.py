class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]

        #approach 1 


        # prod=1
        # temp=0
        # count=0
        # for n in nums:
        #     if(n!=0):

        #         prod=prod*n
        #     else:
        #         temp=1
        #         count=count+1


        # for n in nums:
        #     if(temp==0):
        #         res.append(int(prod/n))
        #     else:
        #         if(n==0 and count!=len(nums) and count<2):
        #             res.append(prod)
        #         elif (count>1):
        #             res.append(0)
        #         else:
        #             res.append(0)

        # return res

        # efficient approch
        pref=1
        res.append(1)
        for i in range(0,len(nums)-1):
            res.append(pref*nums[i])
            pref=pref*nums[i]
        
        post=1
        for i in range(len(nums)-1,0,-1):
            post=post*nums[i]
            res[i-1]=res[i-1]*post
        return res

        
