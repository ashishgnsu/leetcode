class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == " ":
            return True
        else:
            pan= ""
            for i in s.strip():
                if (i >='A' and i <='Z') or (i >= 'a' and i <='z') or (i >='0' and i<= '9'):
                    pan = pan +i
            return pan[::-1].lower() == pan.lower()


