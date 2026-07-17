class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        maxLength = 0
        for i in range(len(s)):
            mySet = set()
            for j in range(i, len(s)):
                if s[j] in mySet:
                    break
                maxLength = max(maxLength, j-i+1)
                mySet.add(s[j])
        return maxLength            
           







                             

        