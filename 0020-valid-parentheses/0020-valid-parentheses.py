class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if (i == '[') or (i == '(') or (i=='{'):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                bracket = stack[-1]   
                if (bracket =='(' and i == ')') or (bracket =='[' and i == ']') or (bracket =='{' and i == '}'):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False    


        