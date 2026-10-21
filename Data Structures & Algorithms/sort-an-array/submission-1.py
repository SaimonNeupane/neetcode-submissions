class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def BuildHeap(A,i,size):
            l=2*i+1
            r=2*i+2
            largest=i
            if l<size and nums[l]>nums[largest]:
                largest=l
            if r<size and nums[r]>nums[largest]:
                largest=r
            if largest!=i:
                nums[i],nums[largest]=nums[largest],nums[i]
                BuildHeap(A,largest,size)
    
        def MaxHeapify(A):
            l=len(A)
            for i in range(l//2,-1,-1):
                BuildHeap(A,i,len(A))


        def HeapSort(A):
            l=len(A)
            size=len(A)
            for i in range(l-1,0,-1):
                A[0],A[i]=A[i],A[0]
                size-=1
                BuildHeap(A,0,size)

            return A
        MaxHeapify(nums)
        return HeapSort(nums)



        




        