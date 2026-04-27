# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=list()
        if root:queue.append(root)
        main_list=list()
        while queue:
            length=len(queue)
            for r in range(length):
                value=queue.pop(0)
                if value.left:queue.append(value.left)
                if value.right:queue.append(value.right)
                if(r==length-1):main_list.append(value.val)
            
        return main_list
        