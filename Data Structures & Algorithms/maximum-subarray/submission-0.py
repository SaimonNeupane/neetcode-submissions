class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=float('-inf')
        temp=0
        for num in nums:
            temp+=num
            
            result=max(result,temp)
            if temp<=0:
                temp=0
        return result
            
        