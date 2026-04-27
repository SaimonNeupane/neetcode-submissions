class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for a,b in enumerate(nums):
            if target-b in seen:
                return [nums.index(target-b),a]
            else:
                seen[b]=a

