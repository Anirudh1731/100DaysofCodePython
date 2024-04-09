class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        subset=[]
        def dfs(ind):
            
            if ind>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[ind])
            dfs(ind+1)
            
            subset.pop()
            dfs(ind+1)
        dfs(0)
        
        return res
        
