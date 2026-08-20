class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "*", "/"]

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
            else:
                stack.append(int(i))
            # print(stack)
        return stack[-1]
