class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total=0
        def neighbours(a,b):
            if a>=len(grid) or b<0 or a<0 or b>=len(grid[0]) or grid[a][b]=="0":
                return
            if grid[a][b]=="1":
                grid[a][b]="0"
            neighbours(a+1,b)
            neighbours(a-1,b)
            neighbours(a,b+1)
            neighbours(a,b-1)

        for a,a_el in enumerate(grid):
            for b,b_el in enumerate(a_el):
                if b_el == "1":
                    print('yes')
                    total+=1
                    neighbours(a,b)
        return total
            