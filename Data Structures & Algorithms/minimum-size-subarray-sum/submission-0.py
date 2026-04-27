class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        temp_sum=0
        if sum(nums)<target:
            return 0
        res=float('inf')
        for r,num in enumerate(nums):
            temp_sum+=num
            while temp_sum>=target:
                res=min(res,r-l+1)
                temp_sum-=nums[l]
                l+=1
           
            
        return res

        