import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth=k
        for i in range(len(nums)):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        self.nums=nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,-val)
        nums=[]
        for i in range(self.kth):
            maxx=heapq.heappop(self.nums)
            nums.append(maxx)
        for num in nums:
            heapq.heappush(self.nums,num)
        return -nums[-1]
        
        
        
