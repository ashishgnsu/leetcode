class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def peak(arr):
            start = 0
            end = len(arr) - 1
            mid = start +(end - start)//2
            while start < end:
                mid = start +(end - start)//2
                if arr[mid] > arr[mid +1]:
                    end = mid
                else:
                    start = mid + 1
                
            return start 

        return peak(arr)                  
        