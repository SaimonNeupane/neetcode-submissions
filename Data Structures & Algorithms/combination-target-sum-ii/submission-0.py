class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res,sol=[],[]
        sett=set()
        n=len(candidates)
        def backtracking(i):
            if sum(sol)==target:
                if(sorted(sol) not in res):
                    res.append(sorted(sol[:]))
                return
            elif i>=n:
                return 
            backtracking(i+1)
            sol.append(candidates[i])
            backtracking(i+1)
            sol.pop()
        backtracking(0)
        return res
        