import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr=[(-a,'a'),(-b,'b'),(-c,'c')]
        arr=[(x,y) for x,y in arr if x<0]
        heapq.heapify(arr)
        res=[]
        while arr:
            y,x=heapq.heappop(arr)
            if len(res)>=2 and res[-1] and res[-2] and res[-1]==res[-2]==x :
                if arr:
                    b,a=heapq.heappop(arr)
                    res.append(a)
                    if b+1<0:
                        heapq.heappush(arr,(b+1,a))
                    heapq.heappush(arr,(y,x))
                else:
                    return "".join(res)
            else:
                res.append(x)
                if y+1<0:
                    heapq.heappush(arr,(y+1,x))
        return "".join(res)
            



        
        