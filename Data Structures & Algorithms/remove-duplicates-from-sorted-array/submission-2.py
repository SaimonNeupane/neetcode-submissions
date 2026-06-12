class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        for x in range(len(nums)-1):
            if nums[l]==nums[r]:
                r+=1
            else:
                l+=1
                nums[l]=nums[r]
                r+=1
        return l+1

            


        
        