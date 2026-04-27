# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=list()
        if root:queue.append(root)
        main_list=list()
        while  queue:
            temp_list=list()
            length=len(queue)
            for i in range(length):
                element=queue.pop(0)
                if element.left:queue.append(element.left)
                if element.right:queue.append(element.right)
                temp_list.append(element.val)
            main_list.append(temp_list)

                
        print(main_list)
        return list(main_list)


        