class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for edge in edges:
            a,b= edge
            adj[a].append(b)
            adj[b].append(a)
        
        visited=set()
        queue=[]
        def bfs(num):
            if num not in visited:
                visited.append(num)
            


        total_island=0
        for i in range(n):
            if i not in visited:
                total_island+=1
                queue.append(i)
                while queue:
                    num=queue.pop(0)
                    if num not in visited:
                        visited.add(num)
                    nums=adj[num]
                    queue=queue+[num for num in nums if num  not in visited]
        return total_island

                    
                
                

                

                
            