class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]

        hashmap={}
        # efficient approach
        for i in range(0,len(nums)):
            if(target-nums[i] in hashmap):
                ans.append(hashmap[target-nums[i]])
                ans.append(i)
                break
            else:
                hashmap[nums[i]]=i
        # ## Brute force
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]==target):
        #             ans.append(i)
        #             ans.append(j)
        #             break
        
        return ans
                    
        
