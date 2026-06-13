import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth=k
        heapq.heapify(nums)
        self.nums=nums
        while len(self.nums)>self.kth:
            heapq.heappop(self.nums)
        print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums)>self.kth:
            heapq.heappop(self.nums)
        return self.nums[0]
        
        
        
