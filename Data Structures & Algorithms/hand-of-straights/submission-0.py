class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dictt=dict()
        for card in hand:
            if card in dictt:
                dictt[card]+=1
            else:
                dictt[card]=1
        
        while dictt:
            least_value=sorted(dictt)
            first=least_value[0]
            for i in range(first,first+groupSize):
                if i not in dictt:
                    return False
                else:
                    dictt[i]-=1
                    if dictt[i]==0:
                        del dictt[i]

        return True
                