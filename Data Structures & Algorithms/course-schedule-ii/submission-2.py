class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj={i:[] for i in range(numCourses)}
        inDegree=[0]*numCourses

        res=[]

        for pre in prerequisites:
            a,b=pre
            inDegree[a]+=1
            adj[b].append(a)

        queue=[]
        for idx,num in enumerate(inDegree):
            if num==0:
                queue.append(idx)
        while queue:
            crs=queue.pop(0)

            res.append(crs)

            for c in adj[crs]:
                inDegree[c]-=1
                if inDegree[c]==0:
                    queue.append(c)

        return res if len(res)==numCourses else []


        