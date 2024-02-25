class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(0,len(nums)+1)]
        print(freq)

        for i in nums:
            count[i]=1+count.get(i,0)
        
        for n,c in count.items():
            freq[c].append(n)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                    if(len(freq[i])!=0):
                        res.append(n)
                        if(len(res)==k):
                            return res

        

        
