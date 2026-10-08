class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # j = 0
        # i = len(nums)//2 -1
        # l = nums[:]
        # while j <= i:
        #     temp = nums[j]
        #     nums[j] = nums[len(nums)-1-j]
        #     nums[len(nums)-1-j] = temp
        #     j+=1
        # l.extend(nums) 
        # return l 

        return nums + nums[::-1]
        