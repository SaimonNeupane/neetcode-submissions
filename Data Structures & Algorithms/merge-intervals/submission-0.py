class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        first=intervals[0][0]
        last=intervals[0][1]
        for x,y in intervals[1:]:
            if x<=last:
                last=max(last,y)

            else:
                res.append([first,last])
                first=x
                last=y
        res.append([first,last])
        return res
        