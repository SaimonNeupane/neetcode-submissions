class Solution:
    

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        my_grid=[]
        def update(r,c,val):
            if (r>=len(grid) or c>=len(grid[0]) or r<0 or c<0 or grid[r][c]==-1):
                return
            elif grid[r][c]==2147483647:
                print('yes')
                grid[r][c]=val+1
                my_grid.append((r,c))
            

            
            
        
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k]==0:
                    my_grid.append((i,k))
        while my_grid:
            j=len(my_grid)
            for _ in range(j):
                r,c=my_grid[0]
                val=grid[r][c]
                my_grid.pop(0)
                update(r+1,c,val)
                update(r-1,c,val)
                update(r,c+1,val)
                update(r,c-1,val)

            

        


        