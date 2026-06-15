import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        tempp=[]
        for i,ps in enumerate(points):
            x,y=ps
            dis=(x**2+y**2)**0.5
            tempp.append((dis,(x,y)))
            
        heapq.heapify(tempp)
        for i in range(k):
            x,y=heapq.heappop(tempp)
            res.append(list(y))
        return res


        