class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        w=min(len(word1),len(word2))
        for x in range(w):
            res+=word1[x]
            res+=word2[x]
        res=res+word1[w:] + word2[w:]
        return res
        

        