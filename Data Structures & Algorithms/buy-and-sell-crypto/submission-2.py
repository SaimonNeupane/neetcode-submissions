class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxx=0
        while r!=(len(prices)):
            if prices[r]<prices[l]:
                temp=0
                l=r
            else:
                temp=prices[r]-prices[l]
                print(f'for r={r} and l={l} price is {temp}')
                maxx=max(temp,maxx)
            r+=1
        return maxx



        
                
         
            
