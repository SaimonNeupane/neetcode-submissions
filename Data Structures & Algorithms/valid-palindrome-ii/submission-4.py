class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        def checkPalindrome(x,y):
            while x<y:
                if s[x]!=s[y]:
                    return False
                x+=1
                y-=1
            return True
        
        while i<j:
            if s[i]!=s[j]:
                return checkPalindrome(i+1,j) or checkPalindrome(i,j-1)
            i+=1
            j-=1
        return True
      

        