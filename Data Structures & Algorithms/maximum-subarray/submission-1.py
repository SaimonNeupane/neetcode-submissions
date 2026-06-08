class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx=float('-inf')
        temp=0
        for num in nums:
            temp+=num
            maxx=max(maxx,temp)
            if temp<=0:
                temp=0
        return maxx
            


        