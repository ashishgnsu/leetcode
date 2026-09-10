class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        first_zero_index = nums1.index(0) if 0 in nums1 else -1
        if first_zero_index != -1:
            j = 0
            for i in range(m, len(nums1)):
                nums1[i] = nums2[j]
                j = j+1   
            nums1.sort()
        return nums1