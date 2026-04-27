class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        curr=-1
        for idx,num in enumerate(reversed(nums)):
           curr+=1
           if num!=0:
              if curr<=num:
                goal-=curr
                curr=0
        return goal==0
              

