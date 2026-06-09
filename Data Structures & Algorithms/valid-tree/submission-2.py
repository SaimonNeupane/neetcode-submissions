class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj={i:[] for i in range(n)}
        visit=set()

        for a in edges:
            a,b=a
            adj[a].append(b)
            adj[b].append(a)
        def dfs(num,parent):
            if num in visit :
                return False
            visit.add(num)
            for n in adj[num]:
                if  n != parent:
                    if not dfs(n,num):
                        return False
            return True
        count=0
        for i in range(n):
            if i not in visit:
                count+=1
                if not dfs(i,i):
                    return False
        return count==1
            
               
            


        
        

        

        