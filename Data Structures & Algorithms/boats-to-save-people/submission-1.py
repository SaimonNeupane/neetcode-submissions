class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # l=max(people)
        # count=[0]*(l+1)
        # for p in people:
        #     count[p]+=1
        # idx,i=0,1
        # while idx<len(people):
        #     while count[i]==0:
        #         i+=1
        #     people[idx]=i
        #     count[i]-=1
        #     idx+=1
        people.sort()
        l=0
        r=len(people)-1
        res=0
        while l<=r:
            inBoat=people[r]
            capacity=limit-inBoat
            if capacity >=people[l]:
                l+=1
            res+=1
            r-=1
        return res
        

            
            
        