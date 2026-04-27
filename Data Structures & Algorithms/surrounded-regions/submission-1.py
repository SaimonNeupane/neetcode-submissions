class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_o=list()
        new_list=list()
        def update(r,c):
            if r>=len(board) or r<0 or c>= len(board[0]) or c<0 or board[r][c]=='X' or board[r][c]=='S':
                return
            else:
                print(r,c)
                print(len(board))
                border_o.append((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if ( r==0 or c==0 or r==len(board)-1 or c==(len(board[0])-1) ) and board[r][c]=='O':
                    border_o.append((r,c))
        while border_o:
            l=len(border_o)
            new_list.append(border_o)
            print('for the iteration')
            for _ in range(l):
                r,c=border_o[0]
                board[r][c]='S'
                border_o.pop(0)
                update(r+1,c)
                update(r-1,c)
                update(r,c-1)
                update(r,c+1)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='S':
                    board[r][c]='O'
                else:
                    board[r][c]='X'

        
        


        