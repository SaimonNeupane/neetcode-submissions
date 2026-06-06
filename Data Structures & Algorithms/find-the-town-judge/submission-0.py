class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num=[0]*(n)
        for a in trust:
            first=a[0]
            second=a[1]
            print(first)
            print(second)
            num[first-1]-=1
            num[second-1]+=1
        

        for i,ns in enumerate(num):
            if ns==n-1:
                return i+1

        return -1
            
                

        