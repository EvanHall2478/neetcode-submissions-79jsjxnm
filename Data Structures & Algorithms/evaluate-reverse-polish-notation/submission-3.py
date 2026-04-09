class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                temp = stack[-1]
                stack.pop()
                if i == "+":
                    temp += stack[-1]
                elif i == "-":
                    temp = stack[-1] - temp
                elif i == "*":
                    temp *= stack[-1]
                elif i == "/":
                    temp = int(stack[-1] / temp)
                    
                stack.pop()
                stack.append(temp)
        return stack[-1]
