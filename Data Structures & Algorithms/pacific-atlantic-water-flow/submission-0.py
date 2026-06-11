class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific=[]
        atlantic=[]
        pacificc=set()
        atlanticc=set()
        for r,h in enumerate(heights):
            for c,x in enumerate(h):
                if r==0 or c==0:
                    pacific.append((r,c))
                if r==len(heights)-1 or c== len(heights[0])-1:
                    atlantic.append((r,c))
        
        def dfs(r,c,prev,sett):
            if heights[r][c]<prev:
                return 
            sett.add((r,c))
            offsets=[(0,1),(0,-1),(1,0),(-1,0)]
            for off in offsets:
                x,y=off
                r_temp,c_temp=r+x,c+y
                if 0<=r_temp<len(heights) and 0<=c_temp<len(heights[0]) and (r_temp,c_temp) not in sett:
                    dfs(r_temp,c_temp,heights[r][c],sett)
            return 
        
        for x in pacific:
            r,c=x
            dfs(r,c,heights[r][c],pacificc)
        for y in atlantic:
            r,c=y
            dfs(r,c,heights[r][c],atlanticc)
            
        res=list(pacificc & atlanticc)
        return [list(x) for x in res]


       
        