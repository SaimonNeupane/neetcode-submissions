class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])

        if m==n==1:
            return word==board[0][0]
        
        def backtrack(r,c,index):
            if index>=len(word):
                return True
            if word[index]!=board[r][c]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            
            for i_off,j_off in [(0,1),(0,-1),(1,0),(-1,0)]:
                r_temp,c_temp=r+i_off,c+ j_off
                if 0<=r_temp<m and 0<=c_temp<n:
                    if  backtrack(r_temp,c_temp,index+1):
                        return True
                    
            board[r][c]=temp
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        return False
        