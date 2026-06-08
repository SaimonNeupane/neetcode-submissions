class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       arr=[0]*(numCourses)
       adj={i:[] for i in range(numCourses)}
       for num in prerequisites:
            a,b=num
            arr[a]+=1
            adj[b].append(a)
       queue=[]
       total=0
       for id,num in enumerate(arr):
            if num==0:
                queue.append(id)
        
       while queue:
            cs=queue.pop(0)
            total+=1
            for neighbour in adj[cs]:
                arr[neighbour]-=1

                if arr[neighbour]==0:
                    queue.append(neighbour)
       return total==numCourses
