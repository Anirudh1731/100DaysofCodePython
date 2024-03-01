class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=i+1

        while(i<len(nums) and j<len(nums)):
            if(nums[i]%2==0):
                i=i+1
                j=j+1
            elif(nums[i]%2!=0 and nums[j]%2==0):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i=i+1
                j=j+1
            else:
                j=j+1

        return nums
