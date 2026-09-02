class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        word = min(strs, key = len)
        
        i = 0
        while i < len(word):
            for words in strs:
                if word[i] != words[i] and word != words:
                    return word[:i]    
            i = i+1                  
        return word







        