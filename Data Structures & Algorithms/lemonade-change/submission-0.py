class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dictt={5:0,10:0,20:0}
        for bill in bills:
            if bill==5:
                dictt[5]+=1
            elif bill==10 and dictt[5]>=1:
                dictt[5]-=1
                dictt[10]+=1
            elif bill==20 and (dictt[10]>=1 and dictt[5]>=1):
                dictt[20]+=1
                dictt[5]-=1
                dictt[10]-=1
            elif bill==20 and (dictt[10]==0 and dictt[5]>=3):
                dictt[5]-=3
            else:
                return False
        return True
            

        