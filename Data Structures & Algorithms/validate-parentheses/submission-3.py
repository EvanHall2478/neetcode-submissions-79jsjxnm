class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        if len(s) == 0:
            return True
        
        stack = []
        # seen_stack = []
        left_braces = ["[", "{", "("]
        right_braces = ["}", "}", ")"]

        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i == ")" and stack[-1] == "(" \
            or i == "]" and stack[-1] == "[" \
            or i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
            