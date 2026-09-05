class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        prefix_max = [nums[0]] * n
        for i in range(1,n):
                prefix_max[i]= max(prefix_max[i-1], nums[i])

        suffix_min = [nums[-1]] * n
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])  
        
        for i in range(0, len(nums)):
            if (prefix_max[i] - suffix_min[i]) <= k:
                return i
        
        return -1
