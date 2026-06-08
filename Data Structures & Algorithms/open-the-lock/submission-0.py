
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1
            
        queue=[("0000",0)]
        print(queue)
        visited=set(deadends)
        i=0
        def get_child(state:str):
            children=[]
            for i in range(4):
                temp=(int(state[i])+1)%10
                children.append(str(state[:i]+str(temp)+ state[i+1:]))
                temp=(int(state[i])-1+10)%10
                children.append(str(state[:i]+str(temp)+ state[i+1:]))
            return children    
        while queue:
            n=len(queue)
            state,turn = queue.pop(0) 
            if state==target:
                return turn
            for s in get_child(state):
                if s not in visited:
                    visited.add(s)
                    queue.append((s,turn+1))
                
        return -1

