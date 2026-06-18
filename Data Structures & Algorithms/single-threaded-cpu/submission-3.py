import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue=[]
        res=[]
        heapq.heapify(queue)
        for i,t in enumerate(tasks):
            t.append(i)
        heapq.heapify(tasks)
        time=0
        while tasks or queue:
            if queue :
                x=heapq.heappop(queue)
                time+=x[0]
                res.append(x[1])
            if tasks:
                time=max(tasks[0][0],time)
                while tasks and tasks[0][0]<=time:
                    t=heapq.heappop(tasks)
                    heapq.heappush(queue,[t[1],t[2]])
        return res