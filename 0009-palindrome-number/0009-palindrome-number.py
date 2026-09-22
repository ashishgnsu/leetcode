class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        reverse = 0
        original_num = x
        
        while x!=0:
            remainder = x%10
            reverse = reverse*10 + remainder
            x/=10

        if original_num == reverse:
            return True
        return False         