import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letters=[0]*26
        queue=deque()
        time=0
        for t in tasks:
            letters[ord(t)-65]-=1
        letters=[count for count in letters if count<0]
        heapq.heapify(letters)
        while letters or queue:
            time+=1   


            while queue and queue[0][1]==time:
                    heapq.heappush(letters,queue[0][0])
                    queue.popleft()
            if letters:
                y=heapq.heappop(letters)
                if y+1<0:
                    queue.append((y+1,time+n+1))
            
        return time




        




        
        