import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)-1
        cols= len(heights[0])-1
        visit=set()
        heap=[(0,0,0)]
        heapq.heapify(heap)
        while heap:
            diff,r,c=heapq.heappop(heap)
            if (r,c) in visit:
                continue
            if (r==rows and c==cols):
                return diff
            visit.add((r,c))
            dirs=[(1,0),(-1,0),(0,1),(0,-1)]
            for x,y in dirs:
                x_off,y_off=r+x,y+c
                if x_off<0 or x_off >=len(heights) or y_off <0 or y_off >=len(heights[0]) or (x_off,y_off) in visit:
                    continue
                else:
                    heapq.heappush(heap,(max(abs(heights[x_off][y_off]-heights[r][c]),diff),x_off,y_off))

                   
        