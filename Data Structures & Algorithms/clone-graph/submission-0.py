"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map=dict()
        def dfs(node):
            if not node:
                return
            if node in  map:
                return map[node]
            
            map[node]=Node(node.val)
            
            for n in node.neighbors:
                map[node].neighbors.append(dfs(n))
            
            return map[node]
        return dfs(node)
        