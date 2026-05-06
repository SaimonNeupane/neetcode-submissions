class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==1:
            return [[s]]
        def isPalindrome(start,end)->bool:
            l,r=start,end
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
                
            return True
        res=[]
        sol=[]
        def backtrack(start:int):
            if start>=len(s):
                res.append(sol[:])
                return
            for i in range(start,len(s)):
                if isPalindrome(start,i):
                    sol.append(s[start:i+1])    
                    backtrack(i+1)
                    sol.pop()
                    
        backtrack(0)
        return res
                    
                

        


            

