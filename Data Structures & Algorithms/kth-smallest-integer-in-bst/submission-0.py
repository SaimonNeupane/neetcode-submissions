# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue=list()
        main_list=list()
        if root:queue.append(root)
        print(queue)
        while queue:
            r=len(queue)
            for i in range(r):
                item=queue.pop(0)
                main_list.append(item.val)
                if item.left: queue.append(item.left)
                if item.right: queue.append(item.right)
        main_list.sort()
        return main_list[k-1]


        