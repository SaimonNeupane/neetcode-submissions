# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ls=list()
        def recurse(node):
            if node is None:
                return 
            
            recurse(node.left)
            ls.append(node.val)
            right=recurse(node.right)
        recurse(root)
        print(ls)
        return  (len(ls)==len(set(ls)))and ls== sorted(ls)
        
            
            
            

        return recurse(root)