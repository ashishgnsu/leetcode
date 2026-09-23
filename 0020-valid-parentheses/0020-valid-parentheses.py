class Stack:
    def __init__(self):
        self.__items = []

    def push(self,item):
        self.__items.append(item)

    def isEmpty(self):
        return len(self.__items) == 0

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop Stack is Empty.")
        else:
            return self.__items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek Stack is Empty.")
        else:
            return self.__items[-1]

    def lenght(self):
        return len(self.__items)      


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for i in s:
            if (i == '[') or (i == '(') or (i=='{'):
                stack.push(i)
            else:
                if stack.isEmpty():
                    return False
                bracket = stack.peek()    
                if (bracket =='(' and i == ')') or (bracket =='[' and i == ']') or (bracket =='{' and i == '}'):
                    stack.pop()
                else:
                    return False

        if stack.isEmpty():
            return True
        return False    


        