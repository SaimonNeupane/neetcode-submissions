import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        letters=[0]*26
        for i , c in enumerate(s):
            letters[ord(c)-97]-=1
        alp='abcdefghijklmnopqrstuvwxyz'
        res=""
        letters=[(x,alp[i]) for i,x in enumerate(letters) if x<0]
        heapq.heapify(letters)
        while letters:
            x,i=heapq.heappop(letters)
            if res and res[-1]==i:
                if letters:
                    y,j=heapq.heappop(letters)
                    res+=j
                    if y+1<0 :
                        heapq.heappush(letters,(y+1,j))
                    heapq.heappush(letters,(x,i))
                else:
                    return ""
                
                
            else:
                res+=i
                if x+1<0:
                    heapq.heappush(letters,(x+1,i))
        return res
        

    
        