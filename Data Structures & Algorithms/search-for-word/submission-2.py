class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        w=len(word)
        if m==1 and n==1:
            return word==board[0][0]

        def backtrack(pos,index):
            r,c=pos
            
            if index==w:
                return True
            if word[index]!=board[r][c]:
                return False
            
            char=board[r][c]
            board[r][c]='#'
            for i_off , j_off in [(0,-1),(0,1),(1,0),(-1,0)]:
                r_,c_=r+i_off,c+j_off
                if r_>=0 and r_<m and c_>=0 and c_<n:
                    if backtrack((r_,c_),index+1):
                        return True
    
            board[r][c]=char
            return False
        

        for i in range(m):
            for j in range(n):
                if backtrack((i,j),0):
                    return True

        return False