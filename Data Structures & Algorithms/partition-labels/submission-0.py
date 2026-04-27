class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictt=dict()
        for idx,char in enumerate(s):
                dictt[char]=idx
        count=0
        idx=0
        result=[]
        for id,char in  enumerate(s):
            temp=dictt[char]
            idx=max(idx,temp)
            count+=1
            if id==idx:
                result.append(count)
                count=0
                
        return result
            

        