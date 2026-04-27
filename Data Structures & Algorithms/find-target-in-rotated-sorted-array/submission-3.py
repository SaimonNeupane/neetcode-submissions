class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0;
        r=len(nums)-1;
        pivot=-1;
        while l<r:
            mid=(l+r)//2
            if(nums[mid]>nums[r]):
                l=mid+1
            elif(nums[mid]<nums[r]):
                r=mid
        # print(l)
        r=len(nums)-1

        if(target>nums[r]):
            r=l;
            l=0;
        while l<=r:
            print('inside loop')
            mid=(l+r)//2
            print(mid)
            if(nums[mid]==target):
                print('year')
                return mid
            if(nums[mid]<target):
                l=l+1
            else:
                r=r-1
        return -1

    

