class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        my_grid=[]
        a=-1
        fresh=0
        def update(r,c):
            if r>=len(grid)or r<0 or c>=len(grid[0]) or c<0 or grid[r][c]==0 or grid[r][c]==2:
                return
            else:
                grid[r][c]=2
                my_grid.append((r,c))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    my_grid.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while my_grid:
            a+=1
            l=len(my_grid)
            print(l)
            for _ in range(l):
                r,c=my_grid[0]
                my_grid.pop(0)
                update(r+1,c)
                update(r-1,c)
                update(r,c-1)
                update(r,c+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return a
        


