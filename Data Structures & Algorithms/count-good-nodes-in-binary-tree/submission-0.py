# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        maxx=root.val
        def dfs(root,maxx):
            if root is None:
                return float('-inf')
            if root.val>=maxx:
                maxx=root.val
                self.count+=1
                max=root.val
            dfs(root.left,maxx)
            dfs(root.right,maxx)
        dfs(root,maxx)
        return self.count
    
