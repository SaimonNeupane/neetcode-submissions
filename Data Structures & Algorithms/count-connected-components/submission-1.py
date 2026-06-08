class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for edge in edges:
            a,b= edge
            adj[a].append(b)
            adj[b].append(a)
        
        visited=set()
        queue=[]
       
        total_island=0
        for i in range(n):
            if i not in visited:
                total_island+=1
                queue.append(i)
                while queue:
                    nums=adj[queue.pop(0)]
                    for num in nums:
                        if num not in visited:
                            visited.add(num)
                            queue.append(num)
                    
        return total_island
    