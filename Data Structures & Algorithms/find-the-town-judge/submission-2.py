class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num=[0]*(n+1)
        for a in trust:
            
            num[a[0]]-=1
            num[a[1]]+=1
        

        for i,ns in enumerate(num):
            if ns==n-1:
                return i

        return -1
            
                

        