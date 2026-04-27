class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        def traverse(a,b):
            if a<0 or b<0 or a>=len(grid) or b>=len(grid[0]) or grid[a][b]==0:
                return 0
            grid[a][b]=0
            return (1+ traverse(a+1,b)+ traverse(a-1,b)  +traverse(a,b+1)+  traverse(a,b-1))
        for a,a_el in enumerate(grid):
            for b,b_el in enumerate(a_el):
                
                if b_el==1:
                    value=traverse(a,b)
                    area=max(value,area)
        return area


        


        