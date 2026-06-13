import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            max=heapq.heappop(stones)
            min=heapq.heappop(stones)
            diff=min-max
            if abs(diff)!=0:
                heapq.heappush(stones,-diff)
        stones.append(0)
        return -stones[0]
        
        

        