class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        length = 0
        substring = dict()

        while right < len(s):
            if s[right] in substring:
                left = max(left, substring[s[right]] + 1)

            length = max(length, right - left + 1)
            substring[s[right]] = right
            right += 1
        return length    



        