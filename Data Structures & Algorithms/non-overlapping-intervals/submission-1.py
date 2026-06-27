class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        x=float('-inf')
        res=0
        for i in (intervals):
            if i[0]<x:
                x=min(i[1],x)
                res+=1
            else:
                x=i[1]

            
        return res
        