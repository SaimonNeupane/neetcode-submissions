class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def BFS(row,col):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]==0:
                return 1
            
            else:
                return 0
        perimeter=0
        for r,row in enumerate(grid):
            for c,element in enumerate(row):
                if element==1:
                    left=BFS(r-1,c)
                    right=BFS(r+1,c)
                    top=BFS(r,c-1)
                    bottom=BFS(r,c+1)
                    temp=left+right+top+bottom
                    perimeter+=temp
        return perimeter
