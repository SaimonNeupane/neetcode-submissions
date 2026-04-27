class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
       
        water=0;
        while l<=r:
            new=min(heights[l],heights[r])*(r-l)
            water=max(water,new)
            if heights[r]>heights[l]:
                l+=1  
            else: r-=1
        return water
