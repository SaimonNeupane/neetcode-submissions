class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        prev=intervals[0][0]
        prev_last=intervals[0][1]
        print(intervals)
        res=[]
        for x,y in intervals[1:]:
            if x>prev_last:
                res.append([prev,prev_last])
                prev=x
                prev_last=y

            else:
                prev_last=max(y,prev_last)
        res.append([prev,prev_last])
        return res
            
       
        