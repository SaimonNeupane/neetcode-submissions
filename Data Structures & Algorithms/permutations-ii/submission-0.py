class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sett,sol={},[]
        sett=set()
        n=len(nums)
        def backtrack(x:int):
            if x>=n:
                sett.add(tuple(sol[:]))
                return
            for i in range(0,len(nums)):
                if i not in sett:
                    sett.add(i)
                    sol.append(nums[i])
                    backtrack(x+1)
                    sol.pop()
                    sett.remove(i)
        backtrack(0)
        return list(sett)
        