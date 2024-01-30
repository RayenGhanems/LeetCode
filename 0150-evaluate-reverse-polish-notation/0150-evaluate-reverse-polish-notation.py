class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "*":
                    result = operand1 * operand2
                else:  
                    result = int(float(operand1) / operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]