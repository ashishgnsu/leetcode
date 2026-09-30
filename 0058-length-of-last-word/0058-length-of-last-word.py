class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0

        if len(s) == 1:
            return 1
        
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                length += 1
            elif(length != 0):
                return length
        
        return length             
         
