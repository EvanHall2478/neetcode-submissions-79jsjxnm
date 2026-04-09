class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 0:
            return True

        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue

            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)
            elif i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i) 
        print(stack)
        if len(stack) == 0:
            return True
        return False