class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=len(nums)-1
        l=0
    

        while l<=r:
            while (nums and nums[r]==val):
                nums.pop(r)
                r-=1
            if nums and  nums[l]== val:
                nums[l]=nums[r]
                r-=1

            l+=1
            
        return r+1
        
    
