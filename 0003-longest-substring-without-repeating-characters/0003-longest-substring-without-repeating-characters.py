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
        while  right < len(s) :
            if s[right] not in substring:
                substring[s[right]] = right
                right += 1
            else:
                if right - left > length:
                    length = right - left 
                left = max(left, substring[s[right]] +1)   #substring[s[right]] + 1
                substring[s[right]] = right
                right +=1
            if right - left > length:
                length = right - left    
        return length         


        