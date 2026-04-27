class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        if sett:
            length=1
        else:
            length=0
        beginning_list=list()
        for num in sett:
            if num-1 not in sett:
                beginning_number=num
                xa=True
                temp=num
                temp_len=1
                while xa:
                    if temp+1  in sett:
                        temp=temp+1
                        temp_len+=1
                    else:
                        xa=False
                length=max(length,temp_len)
                
        return length
                
                
            
                

      
        

        

