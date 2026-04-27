class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dictt=dict()
        length=len(s1)
        for i,s in enumerate(s1):
            if s in s1_dictt:
                s1_dictt[s]+=1
            else:
                s1_dictt[s]=1
        
        s2_dictt=dict()
        l=0
        for r,c in enumerate(s2):
            if r-l>=length:
                s2_dictt[s2[l]]-=1
                if s2_dictt[s2[l]]==0: del s2_dictt[s2[l]]
                l+=1
            if c in s2_dictt: s2_dictt[c]+=1
            else: s2_dictt[c]=1
            if s1_dictt==s2_dictt:
                return True
        return False



        