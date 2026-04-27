class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sett=set()
        l=0
        for r,num in enumerate(nums):
            if r-l>k:
                sett.remove(nums[l])
                l+=1
            if num in sett:
                return True
            else:
                sett.add(num)
        return False
            
        