class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)*2
        res=[0]*l
        for i in range(l):
            res[i]=nums[int(i%(l/2))]
        return res


       
        