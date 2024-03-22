class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        hashset=set()

        for i in nums:
            if(i in hashset):
                return i
            else:
                hashset.add(i)

        
        
