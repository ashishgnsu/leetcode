class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(0, len(nums)):
            hash[nums[i]] = i
              

        for i in range(0, len(nums)):
            n = target - nums[i]
            if n in hash and hash[n] != i:
                return [i, hash[n]]    

