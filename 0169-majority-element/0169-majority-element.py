class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1

        largest = float('-inf')
        value = 0
        for i in nums:
            if d[i] > largest:
                largest = d[i]
                value = i
        return value      

