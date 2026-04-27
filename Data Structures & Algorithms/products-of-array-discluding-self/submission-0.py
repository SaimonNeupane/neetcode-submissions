class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=nums.count(0)
        if(zero>1):
            return [0]*len(nums)
        elif(zero==1):
            product=1
            for num in nums:
                if num==0:
                    continue;
                else:
                    product*=num
            
            return [0 if a!=0 else product for a in nums]
        else:
            product=1
            for num in nums:
                
                    product*=num
            
            return [ int(product/a) for a in nums]




            

            


        