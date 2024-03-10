class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r=0,1

        profit=0

      # if price of r is greater then only profit or else we will shift l to the lowest one 
        while(r<len(prices)):

            if(prices[l]<prices[r]):
                profit=max(profit,prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return profit


        
