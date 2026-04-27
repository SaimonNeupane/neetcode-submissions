class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0;
        maxx=0;
        for r in range(1,len(prices)):
            while(prices[r]<prices[l]):
                l+=1
            maxx=max(maxx,prices[r]-prices[l])
            
        return maxx
               
         
                
         
            
