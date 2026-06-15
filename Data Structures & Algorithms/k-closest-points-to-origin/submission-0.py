import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        for i,ps in enumerate(points):
            x,y=ps
            dis=(x**2+y**2)**0.5
            points[i]=(dis,(x,y))
            
        heapq.heapify(points)
        for i in range(k):
            x,y=heapq.heappop(points)
            res.append(list(y))
        return res


        