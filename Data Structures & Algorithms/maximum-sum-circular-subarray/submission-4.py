class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        temp=0
        if len(nums)==1:
            return nums[0]
        res=float('inf')
        for num in nums:
            temp+=num
            res=min(res,temp)
            if temp>0:
                temp=0
        print(res)
        res_max=float('-inf')
        temp=0
        for num in nums:
            temp+=num
            res_max=max(temp,res_max)
            if temp<0:
                temp=0 
        print(res_max)
        
        if sum(nums)==res:
            return res_max
        return max(sum(nums)-res,res_max)