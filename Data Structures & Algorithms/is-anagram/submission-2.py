class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict=dict()
        tDict=dict()
        for c in s :
            if c in sDict:
                sDict[c]+=1
            else:
                sDict[c]=0
        for x in t:
            if x  in tDict:
                tDict[x]+=1
            else:
                tDict[x]=0

        return  sDict==tDict