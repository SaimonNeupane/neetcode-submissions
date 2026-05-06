class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,sol=[],[]
        visited=[False]*len(nums)
        def backtrack(x):
            if x>= len(nums):
                res.append(sol[:])
                return
            for i in range(0,len(nums)):
                if visited[i]:
                    continue
                if i >0 and nums[i]==nums[i-1] and visited[i-1]:
                    continue
                visited[i]=True
                sol.append(nums[i])
                backtrack(x+1)
                visited[i]=False
                sol.pop()
        backtrack(0)
        return res
       
        