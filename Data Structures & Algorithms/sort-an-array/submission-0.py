class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            l=len(nums)
            mid=l//2
            left=merge_sort(nums[:mid])
            right=merge_sort(nums[mid:])
            return merge(left,right)

        def merge(left,right):
            l_index=0
            r_index=0
            sorted=[]
            while l_index<len(left) and r_index<len(right):
                if left[l_index]<right[r_index]:
                    sorted.append(left[l_index])
                    l_index+=1
                else:
                    sorted.append(right[r_index])
                    r_index+=1
            sorted.extend(left[l_index:])
            sorted.extend(right[r_index:])
            return sorted
        return merge_sort(nums)




        