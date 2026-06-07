class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictt={}
        for i,lett in enumerate(order):
            dictt[lett]=i

        
        for i in range(1,len(words)):
            prev=words[i-1]
            curr=words[i]
            for j in range(min(len(prev),len(curr))):
                if prev[j]!=curr[j]:
                    if dictt[prev[j]] < dictt[curr[j]]:
                        break
                    return False
            else:
                if len(prev)>len(curr):
                    return False

        return True         
                

                

            


       

