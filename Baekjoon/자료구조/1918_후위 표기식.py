import sys

symbol = ['+', '-', '*', '/']
primarySymbol = ['*', '/']

def changeExpression(expression):
    idx = 0
    operatorStack = []
    operandStack = []
    n = len(expression)
    while (idx < n):
        char = expression[idx]
        if char in symbol:
            if len(operatorStack) != 0:
                if operatorStack[-1] == "(":
                    pass
                elif operatorStack[-1] in primarySymbol:
                    temp = operandStack.pop()
                    temp = operandStack.pop() + temp + operatorStack.pop()
                    operandStack.append(temp)
                    if char not in primarySymbol:
                        temp = operandStack.pop()
                        temp = operandStack.pop() + temp + operatorStack.pop()
                        operandStack.append(temp)
                else:
                    if char in primarySymbol:
                        pass
                    else:
                        temp = operandStack.pop()
                        temp = operandStack.pop() + temp + operatorStack.pop()
                        operandStack.append(temp)
            operatorStack.append(char)

        elif char == '(':
            operatorStack.append(char)

        elif char == ')':
            temp = operandStack.pop()
            while (operatorStack[-1] != "("):
                temp_oper = operatorStack.pop()
                temp = operandStack.pop() + temp + temp_oper
            operatorStack.pop()
            operandStack.append(temp)

        else:
            operandStack.append(char)

        idx += 1

    result = operandStack.pop()

    while (len(operatorStack) != 0):
        result = operandStack.pop() + result + operatorStack.pop()
    return result

def main():
    expression = sys.stdin.readline().rstrip()
    print(changeExpression(expression))

if __name__ == "__main__":
    main()