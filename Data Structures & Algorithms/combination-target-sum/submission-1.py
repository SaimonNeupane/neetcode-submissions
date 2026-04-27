class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        def backtrack(i):
            if sum(sol)>target or i >= len(nums):
                return
            elif sum(sol)==target:
                res.append(sol[:])
                return
            sol.append(nums[i])
            backtrack(i)
            sol.pop()
            backtrack(i+1)

                

            
            

        backtrack(0)
        return res
            
            
           
             
        
        