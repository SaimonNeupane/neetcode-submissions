class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictt={s[0]:0}
        l=0
        res=0
        for r in range(0,len(s)):
            if s[r] in dictt:
                dictt[s[r]]+=1
            else:
                dictt[s[r]]=1
            while sum(dictt.values())-max(dictt.values())>k:
                dictt[s[l]]-=1
                if dictt[s[l]]==0:
                    del dictt[s[l]]
                l+=1
           
            res=max(res,r-l+1)
        return res

