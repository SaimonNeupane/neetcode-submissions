# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q :
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val is not q.val:
            return False
        leftCheck=self.isSameTree(p.left,q.left)
        if leftCheck==False:
            return False
        rightCheck=self.isSameTree(p.right,q.right)
        if rightCheck==False:
            return False
        return True
        

        
            
        
        
       
            