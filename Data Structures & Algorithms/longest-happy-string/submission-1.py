import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr=[(-a,'a'),(-b,'b'),(-c,'c')]
        arr=[(x,y) for x,y in arr if x<0]
        heapq.heapify(arr)
        res=""
        prev=""
        last=""
        while arr:
            y,x=heapq.heappop(arr)
            if prev and last and prev==last==x :
                if arr:
                    b,a=heapq.heappop(arr)
                    last=prev
                    prev=a
                    res+=a
                    if b+1<0:
                        heapq.heappush(arr,(b+1,a))
                    heapq.heappush(arr,(y,x))
                else:
                    return res

                
                
            else:
                res+=x
                last=prev
                prev=x
                if y+1<0:
                    heapq.heappush(arr,(y+1,x))
        return res
            



        
        