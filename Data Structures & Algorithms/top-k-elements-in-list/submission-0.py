class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt=dict()
        for b in nums:
            if(b in dictt):
                dictt[b]+=1
            else:
                dictt[b]=1
        temp=sorted(dictt.items(),key=lambda item:item[1],reverse=True)
        output=[]
        for key,value in temp:
            if len(output)==k:
                return output
            else:
                output.append(key)
        return output

        
        