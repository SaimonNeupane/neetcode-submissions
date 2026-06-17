import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n=len(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        return heapq.heappop(nums)
           
        