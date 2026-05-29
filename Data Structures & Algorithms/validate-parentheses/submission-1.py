class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        if len(s) % 2 != 0:
            return False
        else:
            for c in s:
                if c == ')':
                    if (len(stack) == 0 or stack[-1] != '('):
                        return False
                    else:
                        stack.pop()
                if c == ']':
                    if (len(stack) == 0 or stack[-1] != '['):
                        return False
                    else:
                        stack.pop()
                if c == '}':
                    if (len(stack) == 0 or stack[-1] != '{'):
                        return False
                    else:
                        stack.pop()
                if c == '(' or c == '[' or c == '{':
                    stack.append(c)
                    
        if len(stack) != 0:
            return False
        return True