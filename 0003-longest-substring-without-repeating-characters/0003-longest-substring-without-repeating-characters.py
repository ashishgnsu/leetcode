class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        maxi = 0
        left = right = 0
        while right < len(s):
            if s[right] in d:
                left = max(left, d[s[right]]+1)               
            maxi = max(maxi, right - left + 1)
            d[s[right]] = right
            right = right + 1  
        return maxi


           







                             

        